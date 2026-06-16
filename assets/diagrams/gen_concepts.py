# -*- coding: utf-8 -*-
"""1~4장 개념 도식 SVG. 보드와 같은 디자인 시스템."""
import os
OUT = os.path.dirname(os.path.abspath(__file__))
FONT = "'Malgun Gothic','Segoe UI','Apple SD Gothic Neo',sans-serif"
COBOT="#2563EB"; COBOT_BG="#EFF4FF"; FLOW="#0D9488"; FLOW_BG="#E9FBF7"
INK="#1F2430"; SUB="#5B6472"; GRAY="#9AA0A6"; GRAYBG="#F3F4F6"; GBORDER="#C7CBD1"

def esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
def frame(W,H,title):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
            f'<rect x="0" y="0" width="{W}" height="{H}" rx="20" fill="#fff" stroke="#E5E7EB" stroke-width="1.5"/>',
            f'<text x="40" y="48" font-family="{FONT}" font-size="22" font-weight="800" fill="{INK}">{esc(title)}</text>']
def txt(x,y,s,size=14,w="400",fill=INK,anchor="start"):
    return f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}">{esc(s)}</text>'
def box(x,y,w,h,fill,border,rx=14,dash=""):
    d=f'stroke-dasharray="{dash}"' if dash else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{border}" stroke-width="2" {d}/>'
def arrow(x1,y1,x2,y2,color=INK,wd=2.5):
    return (f'<defs><marker id="ah{abs(int(x1+y2))}" markerWidth="10" markerHeight="10" refX="7" refY="3" orient="auto">'
            f'<path d="M0,0 L7,3 L0,6 Z" fill="{color}"/></marker></defs>'
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{wd}" marker-end="url(#ah{abs(int(x1+y2))})"/>')

def c1():
    W,H=980,430; p=frame(W,H,"1장 — 챗봇 vs 에이전트: 같은 한 마디, 다른 결과")
    # input
    p.append(txt(W/2,86,'사용자: "여름 신제품 출시 프로젝트, 시작해줘"',16,"700",INK,"middle"))
    # left chatbot
    lx=60; p.append(box(lx,110,400,250,GRAYBG,GBORDER))
    p.append(txt(lx+20,140,"❌ 챗봇 (질문답변)",16,"800",GRAY))
    p.append(box(lx+24,160,352,60,"#fff",GBORDER,12))
    p.append(txt(lx+44,196,'"무엇을 도와드릴까요?"',15,"600",SUB))
    p.append(arrow(lx+200,228,lx+200,262,GRAY,2))
    p.append(txt(lx+200,290,"되묻고 — 멈춘다",14,"600",GRAY,"middle"))
    p.append(txt(lx+200,322,"일은 사용자 몫으로 남는다",12.5,"400",GRAY,"middle"))
    # right agent
    rx=520; p.append(box(rx,110,400,250,COBOT_BG,COBOT))
    p.append(txt(rx+20,140,"✓ 코봇 (에이전틱)",16,"800",COBOT))
    chain=["목표 이해","스킬·도구 계획","행동(작성)"]
    cy=170
    for i,s in enumerate(chain):
        p.append(box(rx+24,cy,352,40,"#fff",COBOT,10))
        p.append(txt(rx+44,cy+25,f"{i+1}. {s}",14,"600",INK))
        cy+=50
    p.append(box(rx+24,cy,352,46,COBOT,COBOT,10))
    p.append(txt(rx+200,cy+29,"→ 기획서 초안 산출",15,"800","#fff","middle"))
    p.append('</svg>'); return "\n".join(p)

def c2new():
    W,H=980,470; p=frame(W,H,"2장 — 새로 지은 집: 엔진을 바꿔 끼우다")
    # left: classic (legacy)
    lx=50; p.append(box(lx,90,300,300,GRAYBG,GBORDER,16,"6 4"))
    p.append(txt(lx+20,124,"클래식 — 미리 그리는 설계",14.5,"800",GRAY))
    for i,s in enumerate(["Topics · 분기 트리","Prompts · Child agents","구성 탭 9개","흩어진 화면"]):
        p.append(box(lx+20,146+i*56,260,44,"#fff",GBORDER,10))
        p.append(txt(lx+38,174+i*56,s,13.5,"600",SUB))
    # center: rebuild arrow
    p.append(arrow(360,235,432,235,INK,3))
    p.append(txt(396,219,"재건축",12.5,"800",INK,"middle"))
    p.append(txt(396,258,"엔진 교체",11,"600",SUB,"middle"))
    # right: two new rooms
    rx=442
    p.append(box(rx,90,488,140,COBOT_BG,COBOT,16))
    p.append(txt(rx+20,120,"새 에이전트 — 판단하는 코봇",15,"800",COBOT))
    for i,s in enumerate(["자연어 지침 · 단일 화면","향상된 오케스트레이션 항상 ON","Build·Preview·Evaluate·Monitor"]):
        p.append(txt(rx+20,148+i*26,"• "+s,12.5,"500",INK))
    p.append(box(rx,250,488,140,FLOW_BG,FLOW,16))
    p.append(txt(rx+20,280,"새 워크플로우 — 절차의 플로봇",15,"800",FLOW))
    for i,s in enumerate(["비주얼 캔버스 · 버전 히스토리","노드 단위 테스트 · 지능형 액션","agent node로 코봇과 결합"]):
        p.append(txt(rx+20,308+i*26,"• "+s,12.5,"500",INK))
    p.append(txt(W/2,438,"두 경험은 공존하되 서로 이주하지 않는다 — 무엇을 어디서 시작할지가 첫 결정",12.5,"700",INK,"middle"))
    p.append('</svg>'); return "\n".join(p)

def c2():
    W,H=980,470; p=frame(W,H,"3장 — 두 갈래 길: Agent냐 Workflow냐")
    p.append(box(330,70,320,46,"#fff","#D1D5DB",12))
    p.append(txt(490,99,'"What do you want to build?"',15,"700",INK,"middle"))
    p.append(arrow(430,118,250,150,COBOT)); p.append(arrow(560,118,740,150,FLOW))
    # cobot
    cx=60; p.append(box(cx,155,400,270,COBOT_BG,COBOT,18))
    p.append(txt(cx+24,188,"코봇 — Agent",18,"800",COBOT))
    p.append(txt(cx+24,214,"생각하는 동료 · 판단이 운전",13.5,"600",SUB))
    for i,s in enumerate(["목표를 받아 스스로 추론·행동","유연 — 상황마다 다르게","애매하고 새로운 일에 강함"]):
        p.append(txt(cx+24,250+i*32,"• "+s,14,"500",INK))
    p.append(txt(cx+24,400,"예: 리스크 판단 · 맞춤 보고",13,"700",COBOT))
    # flowbot
    fx=520; p.append(box(fx,155,400,270,FLOW_BG,FLOW,6))
    p.append(txt(fx+24,188,"플로봇 — Workflow",18,"800",FLOW))
    p.append(txt(fx+24,214,"실행하는 동료 · 절차가 운전",13.5,"600",SUB))
    for i,s in enumerate(["정해진 순서를 어김없이 집행","결정적 — 같은 입력=같은 출력","틀리면 안 되는 절차에 강함"]):
        p.append(txt(fx+24,250+i*32,"• "+s,14,"500",INK))
    p.append(txt(fx+24,400,"예: 정기 보고 발송 · 결재 라우팅",13,"700",FLOW))
    # agent node link
    p.append(arrow(465,290,515,290,INK,2)); p.append(arrow(515,310,465,310,INK,2))
    p.append(txt(490,335,"agent node",11,"700",INK,"middle"))
    p.append('</svg>'); return "\n".join(p)

def c3():
    W,H=980,430; p=frame(W,H,"4장 — 지침이 곧 실력: 막연함에서 좋은 지침으로")
    lx=60; p.append(box(lx,100,360,260,GRAYBG,GBORDER,16,"6 4"))
    p.append(txt(lx+20,134,"BEFORE — 막연한 지침",15,"800",GRAY))
    p.append(box(lx+24,156,312,60,"#fff",GBORDER,12))
    p.append(txt(lx+40,193,'"프로젝트 잘 도와줘"',16,"600",SUB))
    p.append(txt(lx+24,250,"→ 무엇을, 어디까지, 모르면?",13.5,"500",GRAY))
    p.append(txt(lx+24,278,"→ 코봇이 추측하거나 헤맨다",13.5,"500",GRAY))
    p.append(arrow(430,230,505,230,COBOT,3))
    rx=520; p.append(box(rx,100,400,260,COBOT_BG,COBOT,16))
    p.append(txt(rx+20,134,"AFTER — 좋은 지침 4요소",15,"800",COBOT))
    rows=[("역할","여름 신제품 출시 프로젝트의 PM"),
          ("범위","기획→일정→예산→리스크→보고 / 회계·법무 제외"),
          ("태도","근거를 인용하고 산출물은 정해진 양식으로"),
          ("원칙","모르면 추측 말고 담당자에게 연결")]
    yy=158
    for k,v in rows:
        p.append(box(rx+22,yy,356,42,"#fff",COBOT,10))
        p.append(txt(rx+34,yy+27,k,13.5,"800",COBOT))
        p.append(txt(rx+92,yy+27,v,12.5,"500",INK))
        yy+=48
    p.append('</svg>'); return "\n".join(p)

def c4():
    W,H=980,470; p=frame(W,H,"5장 — 화면은 주장이다: 트레이 7칸을 프로젝트와 잇기")
    # tabs
    tabs=["Build","Preview","Evaluate","Monitor"]; tx=60
    for t in tabs:
        on = t=="Build"
        p.append(box(tx,66,150,34,COBOT if on else "#fff",COBOT,8))
        p.append(txt(tx+75,89,t,13,"700","#fff" if on else COBOT,"middle")); tx+=160
    # center instructions
    p.append(box(60,118,360,320,COBOT_BG,COBOT,16))
    p.append(txt(240,150,"중앙 — Instructions(지침)",15,"800",COBOT,"middle"))
    p.append(txt(240,178,"코봇이 누구인지를 쓰는 캔버스",12.5,"500",SUB,"middle"))
    p.append(box(84,196,312,210,"#fff",COBOT,12))
    for i,s in enumerate(['"여름 신제품 출시 PM…"',"역할·범위·태도·원칙","모를 때 행동 정의","…"]):
        p.append(txt(104,228+i*34,s,13,"500",INK))
    # right tray
    tray=[("Model","두뇌 — 모델"),("Microsoft IQ","조직 데이터 그라운딩"),("Skills","전문성 5종"),
          ("Tools","문서 생성·업로드"),("Knowledge","표준 템플릿·아카이브"),("Connected agents","전문가 팀"),("Memory","나는 PM")]
    yy=118
    for k,v in tray:
        p.append(box(470,yy,450,40,"#fff","#D1D5DB",10))
        p.append(txt(486,yy+25,k,13,"800",INK))
        p.append(txt(690,yy+25,"→ "+v,12.5,"500",SUB))
        yy+=46
    p.append(txt(470,452,"배치가 곧 우선순위 — 화면이 무엇이 중요한지 말한다",12.5,"600",COBOT))
    p.append('</svg>'); return "\n".join(p)

if __name__=="__main__":
    for name,fn in [("concept-ch01",c1),("concept-ch02",c2new),("concept-ch03",c2),("concept-ch04",c3),("concept-ch05",c4)]:
        open(os.path.join(OUT,name+".svg"),"w",encoding="utf-8").write(fn())
        print("wrote",name)
