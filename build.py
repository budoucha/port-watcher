"""Rebuild data.js from cameras.json + japan.topojson.

Run after refreshing source data:
    python build.py
"""
import json
import pathlib

root = pathlib.Path(__file__).parent
cams = json.loads((root / "cameras.json").read_text(encoding="utf-8"))
topo = json.loads((root / "japan.topojson").read_text(encoding="utf-8"))

out = root / "data.js"
with out.open("w", encoding="utf-8") as f:
    f.write("window.JAPAN_TOPO = " + json.dumps(topo, ensure_ascii=False, separators=(",", ":")) + ";\n")
    f.write("window.CAMERAS = " + json.dumps(cams["live_camera_list"], ensure_ascii=False, separators=(",", ":")) + ";\n")

print(f"wrote {out} ({out.stat().st_size} bytes, {len(cams['live_camera_list'])} cameras)")
