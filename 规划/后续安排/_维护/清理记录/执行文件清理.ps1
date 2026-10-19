$ErrorActionPreference = 'Stop'
$cleanupRoot = 'C:\Users\31186\Desktop\未来规划'
$cleanupList = Join-Path $PSScriptRoot '待删除清单.json'
$cleanupLog = Join-Path $PSScriptRoot '逐文件删除结果.jsonl'
$cleanupEntries = @(Get-Content -LiteralPath $cleanupList -Raw -Encoding UTF8 | ConvertFrom-Json)

if ((Resolve-Path -LiteralPath $cleanupRoot).Path -ne $cleanupRoot) { throw '项目路径不匹配' }
if ($cleanupEntries.Count -ne 111) { throw '清单数量不匹配，停止' }
if (@($cleanupEntries.path | Select-Object -Unique).Count -ne 111) { throw '清单存在重复路径，停止' }
if (-not (Test-Path -LiteralPath (Join-Path $PSScriptRoot '清理前文档.zip') -PathType Leaf)) { throw '缺少文档回退包' }

# 先完整验证所有现存目标，避免检查一半就开始删除。
foreach ($cleanupEntry in $cleanupEntries) {
    $cleanupTarget = [IO.Path]::GetFullPath((Join-Path $cleanupRoot $cleanupEntry.path))
    if (-not $cleanupTarget.StartsWith($cleanupRoot + '\', [StringComparison]::OrdinalIgnoreCase)) { throw "路径越界：$cleanupTarget" }
    if ($cleanupTarget.StartsWith((Join-Path $cleanupRoot '.git') + '\', [StringComparison]::OrdinalIgnoreCase)) { throw '禁止删除Git目录文件' }
    if (-not (Test-Path -LiteralPath $cleanupTarget)) { continue }
    $cleanupItem = Get-Item -LiteralPath $cleanupTarget -Force
    if ($cleanupItem.PSIsContainer -or ($cleanupItem.Attributes -band [IO.FileAttributes]::ReparsePoint)) { throw "非普通文件：$cleanupTarget" }
    $cleanupParent = $cleanupItem.Directory
    while ($cleanupParent -and $cleanupParent.FullName -ne $cleanupRoot) {
        if ($cleanupParent.Attributes -band [IO.FileAttributes]::ReparsePoint) { throw "父目录为重解析点：$($cleanupParent.FullName)" }
        $cleanupParent = $cleanupParent.Parent
    }
    if ((Get-FileHash -LiteralPath $cleanupTarget -Algorithm SHA256).Hash.ToLowerInvariant() -ne $cleanupEntry.sha256) { throw "文件已变更：$cleanupTarget" }
    if ($cleanupEntry.retained) {
        $cleanupOriginal = Join-Path $cleanupRoot $cleanupEntry.retained
        if ((Get-FileHash -LiteralPath $cleanupOriginal -Algorithm SHA256).Hash.ToLowerInvariant() -ne $cleanupEntry.sha256) { throw '重复字幕的保留原件已变化' }
    }
}

foreach ($cleanupEntry in $cleanupEntries) {
    $cleanupTarget = [IO.Path]::GetFullPath((Join-Path $cleanupRoot $cleanupEntry.path))
    $cleanupStatus = 'already_missing'
    if (Test-Path -LiteralPath $cleanupTarget -PathType Leaf) {
        if ((Get-FileHash -LiteralPath $cleanupTarget -Algorithm SHA256).Hash.ToLowerInvariant() -ne $cleanupEntry.sha256) { throw "删除前文件变化：$cleanupTarget" }
        # 一次仅删除清单中一个已核hash的普通文件；不递归删目录。
        Remove-Item -LiteralPath $cleanupTarget -Force
        $cleanupStatus = 'deleted'
    }
    [pscustomobject]@{
        path = $cleanupEntry.path
        category = $cleanupEntry.category
        bytes = $cleanupEntry.bytes
        sha256 = $cleanupEntry.sha256
        status = $cleanupStatus
        time_utc = [DateTimeOffset]::UtcNow.ToString('o')
    } | ConvertTo-Json -Compress | Add-Content -LiteralPath $cleanupLog -Encoding UTF8
}

$cleanupRemaining = @($cleanupEntries | Where-Object { Test-Path -LiteralPath (Join-Path $cleanupRoot $_.path) }).Count
Write-Output "清理完成；清单内剩余文件：$cleanupRemaining。目录未递归删除；结果在逐文件删除结果.jsonl。"
