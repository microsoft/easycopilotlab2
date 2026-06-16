# -*- coding: utf-8 -*-
"""코봇·플로봇 성장 보드 SVG 생성기.
각 장이 끝났을 때 코봇/플로봇이 새로 켜진 능력을 보드로 시각화한다.
코봇=파랑/둥근, 플로봇=민트틸/각진. 켜짐=채움, 아직=점선 회색.
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))
FONT = "'Malgun Gothic','Segoe UI','Apple SD Gothic Neo',sans-serif"

# 색
COBOT = "#2563EB"; COBOT_BG = "#EFF4FF"; COBOT_SOFT = "#DBE6FF"
FLOW = "#0D9488"; FLOW_BG = "#E9FBF7"
OFF_FILL = "#F3F4F6"; OFF_BORDER = "#C7CBD1"; OFF_TEXT = "#9AA0A6"
INK = "#1F2430"; SUB = "#5B6472"

COBOT_CELLS = [
    ("env", "환경", "사무실"),
    ("model", "두뇌", "모델"),
    ("instr", "지침", "행동매뉴얼"),
    ("skill", "스킬", "전문성 5종"),
    ("know", "지식·기억", "근거·맥락"),
    ("tool", "도구", "행동"),
    ("team", "전문가팀", "슈퍼호스트"),
]
FLOW_CELLS = [
    ("flow", "워크플로", "정기 절차"),
    ("link", "코봇연결", "agent node"),
    ("trig", "트리거", "무인 가동"),
]

# 장별 켜짐 + 단계 배지
CH = {
    5:  (["env"], ""),
    6:  (["env","model"], ""),
    7:  (["env","model","instr"], "정체성 완성"),
    8:  (["env","model","instr","skill"], "능력 1"),
    9:  (["env","model","instr","skill","know"], "능력 2"),
    10: (["env","model","instr","skill","know","tool"], "능력 3"),
    11: (["env","model","instr","skill","know","tool","team"], "팀장 도약"),
    12: (["env","model","instr","skill","know","tool","team","flow"], "플로봇 합류"),
    13: (["env","model","instr","skill","know","tool","team","flow","link"], "두 길 합류"),
    14: (["env","model","instr","skill","know","tool","team","flow","link","trig"], "무인 운영"),
    15: ("ALL", "검증"),
    16: ("ALL", "검증"),
    17: ("ALL", "검증"),
    18: ("ALL", "운영"),
    19: ("ALL", "운영"),
    20: ("ALL", "운영"),
}
ALL_KEYS = [k for k,_,_ in COBOT_CELLS] + [k for k,_,_ in FLOW_CELLS]

CAPTION = {
    5: "지금 코봇은 — 살 \uc0ac\ubb34\uc2e4(환경)을 얻었다. 아직 비어 있다.",
    6: "지금 코봇은 — 태어났고 두뇌(모델)를 가졌다.",
    7: "지금 코봇은 — 행동매뉴얼까지 갖춰 \uc815\uccb4\uc131이 완성됐다. (능력은 아직)",
    8: "지금 코봇은 — 스킬 5종으로 \ud55c \uba85\uc774 \ud55c \ud300\ucc98\ub7fc 일한다.",
    9: "지금 코봇은 — 회사 자료에 근거하고 사용자를 기억한다.",
    10: "지금 코봇은 — 말에서 \ud589\ub3d9으로. 실제 산출물을 만든다.",
    11: "지금 코봇은 — 전문가 2인을 이끄는 \ud300\uc7a5(슈퍼호스트)이다.",
    12: "이제 플로봇이 태어났다 — 정해진 절차를 어김없이 집행한다.",
    13: "코봇 \u21c4 플로봇 — 판단과 절차가 서로를 부른다.",
    14: "트리거로 \uc0ac\ub78c \uc5c6\uc774 도는 무인 운영이 완성됐다.",
    15: "검증 단계 — Preview로 즉시 확인·교정한다.",
    16: "검증 단계 — 추론(머릿속)을 읽어 고친다.",
    17: "검증 단계 — 품질을 숫자로 증명·개선한다.",
    18: "운영 단계 — 팀이 호출하는 동료로 정식 배치.",
    19: "운영 단계 — 데이터로 자신을 키운다.",
    20: "운영되는 동료 — 조직이 함께 운영하는 자산이 됐다.",
}

def esc(s):
    return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def chip(x, y, w, h, label, sub, on, accent, accent_bg):
    rx = 14
    cx = x + w - 13; cy = y + 13
    if on:
        fill = accent_bg; border = accent; tcol = accent; subcol = SUB; dash = ""
        badge = f'<circle cx="{cx}" cy="{cy}" r="8" fill="{accent}"/>' \
                f'<path d="M {cx-3.5} {cy} l 2.6 2.8 l 5 -6" stroke="#fff" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    else:
        fill = OFF_FILL; border = OFF_BORDER; tcol = OFF_TEXT; subcol = OFF_TEXT
        dash = 'stroke-dasharray="5 4"'; badge = ""
    return f'''<g>
  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{border}" stroke-width="2" {dash}/>
  <text x="{x+w/2}" y="{y+h/2+4}" font-family="{FONT}" font-size="16.5" font-weight="700" fill="{tcol}" text-anchor="middle">{esc(label)}</text>
  <text x="{x+w/2}" y="{y+h/2+23}" font-family="{FONT}" font-size="11" fill="{subcol}" text-anchor="middle">{esc(sub)}</text>
  {badge}
</g>'''

def row(label, cells, lit, accent, accent_bg, x0, y, cw, ch_, gap):
    out = [f'<text x="{x0-18}" y="{y+ch_/2+6}" font-family="{FONT}" font-size="16" font-weight="800" fill="{accent}" text-anchor="end">{label}</text>']
    x = x0
    for k, lab, sub in cells:
        out.append(chip(x, y, cw, ch_, lab, sub, k in lit, accent, accent_bg))
        x += cw + gap
    return "\n".join(out), x

def build(n):
    old = n - 1
    lit_spec, badge = CH[old]
    lit = ALL_KEYS if lit_spec == "ALL" else lit_spec
    W, H = 980, 430
    x0 = 150; cw = 104; gap = 12; ch_ = 70
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">']
    parts.append(f'<rect x="0" y="0" width="{W}" height="{H}" rx="20" fill="#FFFFFF" stroke="#E5E7EB" stroke-width="1.5"/>')
    # title
    parts.append(f'<text x="40" y="50" font-family="{FONT}" font-size="22" font-weight="800" fill="{INK}">코봇 키우기 — {n}장까지의 성장</text>')
    # step badge
    parts.append(f'<rect x="{W-150}" y="28" width="110" height="32" rx="16" fill="{COBOT}"/>'
                 f'<text x="{W-95}" y="49" font-family="{FONT}" font-size="14" font-weight="700" fill="#fff" text-anchor="middle">{n} / 21단계</text>')
    if badge:
        parts.append(f'<rect x="{W-150}" y="66" width="110" height="28" rx="14" fill="{FLOW_BG if old>=12 else COBOT_BG}" stroke="{FLOW if old>=12 else COBOT}" stroke-width="1.5"/>'
                     f'<text x="{W-95}" y="85" font-family="{FONT}" font-size="12.5" font-weight="700" fill="{FLOW if old>=12 else COBOT}" text-anchor="middle">{esc(badge)}</text>')
    # cobot row
    r1, _ = row("코봇", COBOT_CELLS, lit, COBOT, COBOT_BG, x0, 96, cw, ch_, gap)
    parts.append(r1)
    # divider
    parts.append(f'<line x1="40" y1="200" x2="{W-40}" y2="200" stroke="#EEF0F3" stroke-width="1.5"/>')
    # flow row
    r2, _ = row("플로봇", FLOW_CELLS, lit, FLOW, FLOW_BG, x0, 226, cw, ch_, gap)
    parts.append(r2)
    # flow note (still off)
    if lit_spec != "ALL" and not any(k in lit for k,_,_ in FLOW_CELLS):
        parts.append(f'<text x="{x0+3*(cw+gap)+20}" y="266" font-family="{FONT}" font-size="13" fill="{OFF_TEXT}">아직 등장 전 — 4부에서 합류</text>')
    # caption bar
    parts.append(f'<rect x="40" y="332" width="{W-80}" height="58" rx="14" fill="{COBOT_BG if old<12 else FLOW_BG}"/>')
    parts.append(f'<text x="{W/2}" y="368" font-family="{FONT}" font-size="16.5" font-weight="700" fill="{INK}" text-anchor="middle">{esc(CAPTION[old])}</text>')
    # footer legend
    parts.append(f'<text x="40" y="414" font-family="{FONT}" font-size="11.5" fill="{SUB}">● 켜짐 = 이번 장까지 갖춘 능력   ◌ 점선 = 다음 장부터</text>')
    parts.append('</svg>')
    return "\n".join(parts)

if __name__ == "__main__":
    for n in range(6, 22):
        svg = build(n)
        p = os.path.join(OUT, f"board-ch{n:02d}.svg")
        with open(p, "w", encoding="utf-8") as f:
            f.write(svg)
        print("wrote", p)
