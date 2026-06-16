# -*- coding: utf-8 -*-
"""SVG -> PNG 렌더 (headless chromium). 인자로 받은 svg 파일들을 같은 이름 .png로."""
import sys, os, glob, base64
from playwright.sync_api import sync_playwright

def render(paths, scale=2):
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(device_scale_factor=scale)
        for sp in paths:
            svg = open(sp, encoding="utf-8").read()
            html = f'<!doctype html><meta charset="utf-8"><body style="margin:0;display:inline-block">{svg}</body>'
            pg.set_content(html)
            el = pg.query_selector("svg")
            out = os.path.splitext(sp)[0] + ".png"
            el.screenshot(path=out)
            print("png", os.path.basename(out))
        b.close()

if __name__ == "__main__":
    args = sys.argv[1:]
    files = []
    for a in args:
        files += glob.glob(a)
    if not files:
        files = glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "*.svg"))
    render(files)
