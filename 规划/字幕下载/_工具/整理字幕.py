import importlib.util
import json
import re
import sys
from dataclasses import asdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent
MODEL = ROOT / "_工具/bilinote/transcriber_model.py"
spec = importlib.util.spec_from_file_location("bilinote_transcript_model", MODEL)
model = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = model
spec.loader.exec_module(model)


def normalize(title):
    return title.casefold().replace("一w", "1w")


def seconds(timestamp):
    h, m, s, ms = map(int, re.split(r"[:,]", timestamp))
    return h * 3600 + m * 60 + s + ms / 1000


assert normalize("实习一W") == normalize("实习1w")
assert seconds("00:01:02,500") == 62.5
records = json.loads((ROOT / "_日志/下载结果.json").read_text(encoding="utf-8"))
selected, excluded = [], []
archive = ROOT.parent / "字幕下载_排除项暂存"
foreign = ROOT / "其他语言字幕"
structured = ROOT / "_日志/BiliNote转录结构"
structured.mkdir(exist_ok=True)
for record in records:
    title = record["title"]
    hits = [k for k in ["一W（含1W/1w）", "大二"]
            if ("1w" if k.startswith("一W") else k) in normalize(title)]
    record["排除关键词"] = hits
    if hits:
        archive.mkdir(exist_ok=True)
        for file in ROOT.glob(f"*{record['bvid']}*.srt"):
            destination = archive / file.name
            assert file.resolve().is_relative_to(ROOT)
            assert destination.resolve().is_relative_to(ROOT.parent)
            assert not destination.exists()
            file.rename(destination)
        excluded.append(record)
        continue
    files = list(ROOT.glob(f"*{record['bvid']}*.ai-zh.srt"))
    assert len(files) == 1, (record["bvid"], files)
    file = files[0]
    content = file.read_text(encoding="utf-8-sig").strip()
    assert "\ufffd" not in content
    segments = []
    for block in re.split(r"\n\s*\n", content):
        lines = block.splitlines()
        assert len(lines) >= 3 and lines[0].isdigit(), block
        start, end = lines[1].split(" --> ")
        segment = model.TranscriptSegment(seconds(start), seconds(end), "\n".join(lines[2:]))
        assert 0 <= segment.start < segment.end and segment.text.strip()
        assert not segments or segment.start >= segments[-1].start
        segments.append(segment)
    assert segments
    result = model.TranscriptResult("zh", "\n".join(s.text for s in segments), segments,
                                   {"source": "Bilibili AI subtitles via BBDownNext v2.3.0",
                                    "url": f"https://www.bilibili.com/video/{record['bvid']}",
                                    "title": title})
    (structured / f"{record['bvid']}.json").write_text(
        json.dumps(asdict(result), ensure_ascii=False, indent=2), encoding="utf-8")
    textfile = file.with_suffix(".txt")
    textfile.write_text(f"{title}\n{result.raw['url']}\n来源：B站AI识别字幕，未经人工校对。\n\n{result.full_text}\n",
                        encoding="utf-8-sig")
    record.update({"中文字幕": file.name, "纯文本": textfile.name,
                   "字幕条数": len(segments), "末条结束秒": segments[-1].end})
    selected.append(record)

for file in ROOT.glob("*.srt"):
    if not file.name.endswith(".ai-zh.srt"):
        foreign.mkdir(exist_ok=True)
        destination = foreign / file.name
        assert not destination.exists()
        file.rename(destination)

assert len(selected) == 13 and len(excluded) == 3
assert len(list(ROOT.glob("*.srt"))) == len(selected)
assert len(list(ROOT.glob("*.txt"))) == len(selected)
summary = {"包含关键词": ["29岁", "双非", "68W年薪"], "包含逻辑": "任意一个命中，忽略大小写",
           "排除关键词": ["一W", "1W", "大二"], "最终下载": selected, "已排除": excluded}
(ROOT / "_日志/最终清单.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
lines = ["# 字幕下载清单", "", "下载日期：2026-10-19（北京时间）", "",
         "合集：https://space.bilibili.com/1798598537/lists/8962861?type=season", "",
         "规则：标题包含“29岁”“双非”“68W年薪”任意一个，忽略大小写；排除“一W”（同时识别1W/1w）或“大二”。",
         "", "合集25个视频；包含关键词命中16个；排除3个；最终保留13个视频的中文字幕和纯文本。", "",
         "- `.ai-zh.srt`：BBDownNext v2.3.0直接下载的B站AI识别字幕，保留原始时间轴。",
         "- `.ai-zh.txt`：使用BiliNote的TranscriptSegment/TranscriptResult数据模型整理出的逐句纯文本。",
         "- `其他语言字幕/`：BBDown同时返回的其他语言版本。",
         "- `_日志/`：原始合集列表、筛选结果、下载日志、结构化转录和最终清单。",
         "- `_工具/`：下载器及BiliNote源码归档和采用的数据模型；未部署BiliNote笔记服务或重新语音识别。",
         "", "工具来源：[BBDownNext](https://github.com/KaiHuaDou/BBDownNext)、[BiliNote](https://github.com/apideed/bilinote)。",
         "", "验证：13份中文字幕均非空，UTF-8解码正常，无替换字符，时间轴格式和顺序有效；未逐句对照音频，AI字幕可能有识别错误。", "",
         "## 已下载", "", "| 视频 | 匹配关键词 | 字幕条数 | 中文字幕 | 纯文本 |", "|---|---|---:|---|---|"]
from urllib.parse import quote
for r in selected:
    title = r["title"].replace("|", " / ")
    lines.append(f"| [{title}](https://www.bilibili.com/video/{r['bvid']}) | {'、'.join(r['匹配关键词'])} | {r['字幕条数']} | [SRT]({quote(r['中文字幕'])}) | [TXT]({quote(r['纯文本'])}) |")
lines.extend(["", "## 已排除", "", "更改筛选条件前已下载的3项移到同级 `字幕下载_排除项暂存/`，不计入交付。", ""])
for r in excluded:
    lines.append(f"- {r['title'].replace('|', ' / ')}（{r['bvid']}）：{'、'.join(r['排除关键词'])}")
(ROOT / "下载清单.md").write_text("\n".join(lines) + "\n", encoding="utf-8-sig")
print(json.dumps({"保留": len(selected), "排除": len(excluded),
                  "中文SRT": len(list(ROOT.glob('*.srt'))), "TXT": len(list(ROOT.glob('*.txt'))),
                  "字幕总条数": sum(r["字幕条数"] for r in selected),
                  "每项覆盖": [{"BV": r["bvid"], "视频秒": r["duration"], "字幕末秒": r["末条结束秒"]} for r in selected]}, ensure_ascii=False, indent=2))
