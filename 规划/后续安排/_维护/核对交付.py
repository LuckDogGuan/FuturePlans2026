"""核对文档与日程；记录来源和输出hash，不验证尚未执行的学习实验。"""
from pathlib import Path
from datetime import date, timedelta
from urllib.parse import unquote
import hashlib
import json
import re
import runpy
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT.parents[1]
data = runpy.run_path(str(ROOT / '_维护' / '生成周计划.py'))
schedule = json.loads((ROOT / '_维护' / '日程核对.json').read_text(encoding='utf-8'))
assert len(schedule) == len(data['WEEKS']) == 40
assert [v['week'] for v in schedule] == list(range(1, 41))
assert len(list((ROOT / '阶段总结').glob('*.md'))) == 8
previous_end = None
for row in schedule:
    start, end = date.fromisoformat(row['start']), date.fromisoformat(row['end'])
    assert start.weekday() == 0 and end - start == timedelta(days=6)
    assert not data['overlaps'](start, end), row
    assert previous_end is None or start > previous_end
    previous_end = end
    path = ROOT / row['file']
    text = path.read_text(encoding='utf-8')
    assert str(start) in text and str(end) in text
    assert all(key in text for key in ['工作问题', '官方阅读', '周二 2h', '周六 5h', '故障', '本周必过项', '选看与延期'])
    assert 'http' in text

distillation = PROJECT / '规划' / '蒸馏'
package = distillation / 'chip-software-framework'
if package.exists():
    from urllib.parse import quote
    rows = ['# 语料清单', '', '2026-10-19。10套视频、20份TXT/SRT；不是10个独立人物/访谈。AI字幕未逐句听核。原文件与副本逐字节SHA256一致。', '', '| 视频 | TXT | SRT |', '|---|---|---|']
    corpus = []
    for source in sorted((PROJECT / '规划' / '保留字幕').glob('*.ai-zh.txt')):
        video = re.search(r'(BV[0-9A-Za-z]+)', source.name).group(1)
        pair = source.with_suffix('.srt')
        for original in (source, pair):
            copied = package / 'references' / 'sources' / 'transcripts' / original.name
            assert original.read_bytes() == copied.read_bytes(), original
            corpus.append({'video': video, 'file': str(copied.relative_to(package)), 'sha256': hashlib.sha256(copied.read_bytes()).hexdigest()})
        txt_url = quote('sources/transcripts/' + source.name, safe='/')
        srt_url = quote('sources/transcripts/' + pair.name, safe='/')
        rows.append(f'| [{video}](https://www.bilibili.com/video/{video}) | [TXT]({txt_url}) | [SRT]({srt_url}) |')
    (package / 'references' / '语料清单.md').write_text('\n'.join(rows) + '\n', encoding='utf-8')
    (package / 'references' / '语料哈希.json').write_text(json.dumps(corpus, ensure_ascii=False, indent=2), encoding='utf-8')

kept_reference_files = [PROJECT / p for p in [
    'README.md', '01_方向选择/我的条件与边界.md', '01_方向选择/职业规划要求汇总.md',
    '03_学习路线/岗位与投递记录.md', '04_参考资料/当前条件简明复核.md',
    '04_参考资料/怎样找职业证据.md', '04_参考资料/研究附录_B站课程与关键词.md',
    '04_参考资料/半导体大厂岗位地图_2026-10-05补充.md',
    '04_参考资料/半导体研究_AMD_Intel_NVIDIA岗位.md',
    '04_参考资料/半导体研究_国内公司与转行岗位.md',
    '05_历史记录/修订记录.md', '规划/字幕下载/下载清单.md',
]]
outputs = sorted(set(list(ROOT.rglob('*.md')) + list(distillation.rglob('*.md')) + kept_reference_files))
broken, link_count = [], 0
for path in outputs:
    text = path.read_text(encoding='utf-8')
    assert '\ufffd' not in text, str(path)
    assert text.count('```') % 2 == 0, f'代码围栏未成对: {path}'
    for match in re.finditer(r'\[[^\]\n]+\]\(([^)\n]+)\)', text):
        target = match.group(1).strip().strip('<>')
        if re.match(r'^(https?://|mailto:|#|codex:)', target):
            continue
        link_count += 1
        target_path = unquote(target.split('#')[0])
        target_path = re.sub(r':\d+$', '', target_path)
        if not (path.parent / target_path).exists():
            broken.append({'file': str(path.relative_to(PROJECT)), 'target': target})
assert not broken, json.dumps(broken, ensure_ascii=False)

def file_info(path):
    raw = path.read_bytes()
    return {'file': str(path.relative_to(PROJECT)), 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}

inputs = sorted((PROJECT / '规划' / '保留字幕').glob('*.ai-zh.*'))
inputs += [PROJECT / p for p in [
    '学习注意.md', 'README.md', '01_方向选择/职业规划要求汇总.md',
    '01_方向选择/我的条件与边界.md', '04_参考资料/研究附录_B站课程与关键词.md',
    '04_参考资料/项目核查/脊柱项目_代码与对话核查.md',
]]
assert len(list((PROJECT / '规划' / '保留字幕').glob('*.ai-zh.txt'))) == 10
assert len(list((PROJECT / '规划' / '保留字幕').glob('*.ai-zh.srt'))) == 10
(ROOT / '_维护' / '输入来源快照.json').write_text(json.dumps([file_info(p) for p in inputs], ensure_ascii=False, indent=2), encoding='utf-8')
result = {
    'checked_on': '2026-10-19', 'learning_weeks': 40, 'stage_files': 8,
    'subtitle_sets': 10, 'distillation_files': len(list(distillation.glob('*.md'))), 'markdown_files': len(outputs),
    'local_links_checked': link_count, 'broken_local_links': broken,
    'holiday_overlaps': 0, 'utf8_replacement_characters': 0,
    'core_end': schedule[19]['end'], 'all_end': schedule[-1]['end'],
    'checks_scope': '文档结构、UTF8、相对链接、日程一致性；未运行学习实验，未逐集验证视频播放/字幕',
}
cleanup_list = ROOT / '_维护' / '清理记录' / '待删除清单.json'
if cleanup_list.exists():
    cleanup_entries = json.loads(cleanup_list.read_text(encoding='utf-8'))
    assert len(cleanup_entries) == 111
    remaining = [v for v in cleanup_entries if (PROJECT / v['path']).exists()]
    result['cleanup_planned_files'] = len(cleanup_entries)
    result['cleanup_remaining_files'] = len(remaining)
    cleanup_log = cleanup_list.with_name('逐文件删除结果.jsonl')
    logged_deletions = {}
    if cleanup_log.exists():
        targets = {v['path']: v for v in cleanup_entries}
        for line in cleanup_log.read_text(encoding='utf-8-sig').splitlines():
            if not line.strip():
                continue
            entry = json.loads(line)
            assert entry['path'] in targets
            assert entry['sha256'] == targets[entry['path']]['sha256']
            assert entry['status'] in ('deleted', 'already_missing')
            if entry['status'] == 'deleted':
                logged_deletions[entry['path']] = entry
    result['cleanup_logged_deleted_files'] = len(logged_deletions)
    result['cleanup_logged_deleted_bytes'] = sum(v['bytes'] for v in logged_deletions.values())
    result['cleanup_status'] = ('completed_with_file_log' if not remaining and len(logged_deletions) == len(cleanup_entries)
                                else 'incomplete_or_execution_log_needs_review')
(ROOT / '_维护' / '检查结果.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
files = outputs + sorted((ROOT / '_维护').glob('*.py'))
files += [ROOT / '_维护' / p for p in ['日程核对.json', '输入来源快照.json', '检查结果.json']]
if package.exists():
    files += sorted((package / 'references' / 'sources' / 'transcripts').glob('*'))
    files += [package / 'references' / '语料哈希.json']
(ROOT / '_维护' / '交付文件清单.json').write_text(json.dumps([file_info(p) for p in files], ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(result, ensure_ascii=True))
