# Décors cartoon 1920x1080 — contours épais, couleurs franches, sol en bas pour poser les personnages.
import random, math
W,H=1920,1080
O='#2B2245'          # couleur des contours
def svg(defs,body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<defs>{defs}
<filter id="blur40"><feGaussianBlur stdDeviation="40"/></filter>
<filter id="blur12"><feGaussianBlur stdDeviation="12"/></filter>
<filter id="glow"><feGaussianBlur stdDeviation="18" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>{body}</svg>'''
def lg(id,stops,x1=0,y1=0,x2=0,y2=1):
    s=''.join(f'<stop offset="{o}" stop-color="{c}"/>' for o,c in stops)
    return f'<linearGradient id="{id}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">{s}</linearGradient>'
def rg(id,stops,cx=.5,cy=.5,r=.5):
    s=''.join(f'<stop offset="{o}" stop-color="{c}" stop-opacity="{a}"/>' for o,c,a in stops)
    return f'<radialGradient id="{id}" cx="{cx}" cy="{cy}" r="{r}">{s}</radialGradient>'
def st(w=7,c=O):return f'stroke="{c}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"'
def cloud(x,y,s=1,fill='#FFFFFF'):
    # nuage cartoon : bosses + base plate
    p=f'M{x-120*s},{y+40*s} q-50,0 -50,-45 q0,-45 55,-45 q10,-60 80,-60 q50,0 70,40 q25,-45 85,-35 q60,10 60,70 q55,5 50,50 q-5,25 -40,25 z'
    # chemin relatif écrit pour s=1, on applique une transformation
    return f'<g transform="translate({x},{y}) scale({s}) translate({-x},{-y})"><path d="M{x-120},{y+40} q-50,0 -50,-45 q0,-45 55,-45 q10,-60 80,-60 q50,0 70,40 q25,-45 85,-35 q60,10 60,70 q55,5 50,50 q-5,25 -40,25 z" fill="{fill}" {st(6)}/><path d="M{x-95},{y+18} q60,14 150,4" fill="none" stroke="#D9ECFF" stroke-width="8" stroke-linecap="round"/></g>'
def stars(n,seed,x0,y0,x1,y1,col='#FFF6C9'):
    r=random.Random(seed);out=[]
    for i in range(n):
        x=r.uniform(x0,x1);y=r.uniform(y0,y1);s=r.choice([2,2,3,3,4,6])
        if s>=6:
            out.append(f'<path d="M{x},{y-14} L{x+4},{y-4} L{x+14},{y} L{x+4},{y+4} L{x},{y+14} L{x-4},{y+4} L{x-14},{y} L{x-4},{y-4} Z" fill="{col}"/>')
        else: out.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{s}" fill="{col}" opacity="{r.uniform(.5,1):.2f}"/>')
    return ''.join(out)
def hill(y,amp,col,seed,k=3,stroke=True):
    r=random.Random(seed);pts=[];n=8
    for i in range(n+1):
        pts.append((i*W/n, y+r.uniform(-amp,amp)))
    d=f'M-20,{H+20} L-20,{pts[0][1]:.0f} '
    for i in range(1,len(pts)):
        x0,y0=pts[i-1];x1,y1=pts[i];cx=(x0+x1)/2
        d+=f'Q{x0+ (x1-x0)*.5:.0f},{min(y0,y1)-amp*.6:.0f} {x1:.0f},{y1:.0f} '
    d+=f'L{W+20},{H+20} Z'
    return f'<path d="{d}" fill="{col}" {st(6) if stroke else ""}/>'
def palm(x,y,h,lean=1,scale=1):
    tx=x+lean*h*.30;ty=y-h
    cx1,cy1=x+lean*h*.02,y-h*.45;cx2,cy2=x+lean*h*.32,y-h*.6
    def pt(t):
        u=1-t;return (u**3*x+3*u*u*t*cx1+3*u*t*t*cx2+t**3*tx, u**3*y+3*u*u*t*cy1+3*u*t*t*cy2+t**3*ty)
    path=f'M{x},{y} C{cx1},{cy1} {cx2},{cy2} {tx},{ty}'
    out=f'<path d="{path}" fill="none" stroke="{O}" stroke-width="58" stroke-linecap="round"/><path d="{path}" fill="none" stroke="#C98A4B" stroke-width="44" stroke-linecap="round"/>'
    for k in range(1,11):
        px,py=pt(k/11);out+=f'<path d="M{px-20:.0f},{py+4:.0f} q20,12 40,0" fill="none" stroke="#8A5229" stroke-width="6" stroke-linecap="round"/>'
    fr=[]
    for ang,ln in [(-200,200),(-160,240),(-120,250),(-75,220),(-30,250),(8,230),(35,190)]:
        a=math.radians(ang);ex=tx+math.cos(a)*ln;ey=ty+math.sin(a)*ln*.5+70
        mx=tx+math.cos(a)*ln*.5;my=ty+math.sin(a)*ln*.5-40
        fr.append(f'<path d="M{tx},{ty} Q{mx},{my-30} {ex},{ey} Q{mx+10},{my+25} {tx},{ty+10} Z" fill="#3FBF5A" {st(6)}/>')
        fr.append(f'<path d="M{tx},{ty+4} Q{mx},{my-6} {ex},{ey}" fill="none" stroke="#2A9A44" stroke-width="5"/>')
    coco=''.join(f'<circle cx="{tx+dx}" cy="{ty+dy}" r="17" fill="#7A4A23" {st(5)}/>' for dx,dy in [(-14,16),(14,18),(0,30)])
    return f'<g transform="translate({x},{y}) scale({scale}) translate({-x},{-y})">{out}{"".join(fr)}{coco}</g>'
def pine(x,y,h,col='#2E8B57',snow=False):
    w=h*.42;out=f'<rect x="{x-14}" y="{y-h*.18}" width="28" height="{h*.2}" fill="#7A4A23" {st(5)}/>'
    for i,(yy,ww) in enumerate([(0.18,1),(0.42,.8),(0.64,.58)]):
        by=y-h*yy;tw=w*ww
        out+=f'<path d="M{x-tw},{by} L{x},{by-h*.42} L{x+tw},{by} Q{x},{by+18} {x-tw},{by} Z" fill="{col}" {st(6)}/>'
        if snow: out+=f'<path d="M{x-tw*.55},{by-h*.17} L{x},{by-h*.42} L{x+tw*.55},{by-h*.17} q-14,14 -28,2 q-14,14 -28,0 q-16,14 -30,0 q-14,14 -28,0 z" fill="#FFFFFF" {st(4)}/>'
    return out

S={}
# ---------------------------------------------------------------- 1. PLAGE
d=lg('sky',[(0,'#3FB6F2'),(.6,'#9FE3FF'),(1,'#D8F6FF')])+lg('sea',[(0,'#1FB5C9'),(1,'#0E8FB5')])+lg('sand',[(0,'#FFE29A'),(1,'#F7C565')])+rg('sun',[(0,'#FFF3A6',1),(.55,'#FFD84A',1),(1,'#FFD84A',0)])
b=f'<rect width="{W}" height="{H}" fill="url(#sky)"/>'
b+=f'<circle cx="1560" cy="230" r="230" fill="url(#sun)" opacity=".6"/>'
b+=''.join(f'<path d="M1560,230 L{1560+math.cos(math.radians(a))*260:.0f},{230+math.sin(math.radians(a))*260:.0f}" stroke="#FFE36B" stroke-width="18" stroke-linecap="round" opacity=".7"/>' for a in range(0,360,30))
b+=f'<circle cx="1560" cy="230" r="120" fill="#FFD84A" {st(8)}/><circle cx="1525" cy="200" r="34" fill="#FFF1A0"/>'
b+=cloud(380,210,1.1)+cloud(900,140,.75)+cloud(1220,300,.6)
b+=f'<path d="M-20,560 L{W+20},560 L{W+20},780 L-20,780 Z" fill="url(#sea)" {st(7)}/>'
b+=f'<path d="M1180,560 q60,-70 150,-60 q90,10 120,60 Z" fill="#5CC46E" {st(6)}/>'+palm(1330,560,120,1,.5)
for i,y in enumerate([600,640,690,735]):
    b+=''.join(f'<path d="M{x},{y} q30,-16 60,0 q30,16 60,0" fill="none" stroke="#FFFFFF" stroke-width="7" stroke-linecap="round" opacity=".75"/>' for x in range(-40+(i%2)*90,W,300))
b+=f'<path d="M-20,760 Q320,700 700,745 T1400,730 T{W+20},720 L{W+20},{H+20} L-20,{H+20} Z" fill="url(#sand)" {st(7)}/>'
b+=f'<path d="M-20,760 Q320,700 700,745 T1400,730 T{W+20},720" fill="none" stroke="#FFFFFF" stroke-width="16" stroke-linecap="round" opacity=".9" transform="translate(0,-12)"/>'
r=random.Random(3)
b+=''.join(f'<circle cx="{r.uniform(0,W):.0f}" cy="{r.uniform(820,1070):.0f}" r="4" fill="#E2A94A" opacity=".6"/>' for _ in range(120))
b+=palm(170,1000,560,1.15,1)
# parasol + serviette
b+=f'<path d="M1500,990 L1460,640" stroke="{O}" stroke-width="24" stroke-linecap="round"/><path d="M1500,990 L1460,640" stroke="#FFFFFF" stroke-width="12" stroke-linecap="round"/>'
b+=f'<path d="M1240,690 Q1300,520 1460,520 Q1620,520 1690,680 Q1640,650 1600,682 Q1550,640 1490,676 Q1420,640 1370,680 Q1310,650 1240,690 Z" fill="#FF5A5A" {st(7)}/>'
b+=f'<path d="M1370,680 Q1380,560 1460,520 Q1430,600 1490,676 M1600,682 Q1570,570 1460,520" fill="none" {st(6)}/><path d="M1390,620 Q1420,560 1460,525 Q1450,600 1480,660 Z M1570,640 Q1540,570 1462,524 Q1520,560 1600,682 Z" fill="#FFFFFF" opacity=".9"/>'
b+=f'<path d="M1300,960 L1700,935 L1745,1020 L1330,1050 Z" fill="#3BA7FF" {st(6)}/>'+''.join(f'<path d="M{1300+i*80+10},{958-i*5} L{1335+i*82+12},{1048-i*6}" stroke="#FFFFFF" stroke-width="14"/>' for i in range(5))
# ballon
b+=f'<g transform="translate(1120,975)"><circle r="58" fill="#FFFFFF" {st(6)}/><path d="M-58,0 A58,58 0 0 1 0,-58 L0,0 Z" fill="#FF5A5A"/><path d="M0,58 A58,58 0 0 1 -58,0 L0,0 Z" fill="#FFD43B"/><path d="M58,0 A58,58 0 0 1 0,58 L0,0Z" fill="#3BA7FF"/><circle r="58" fill="none" {st(6)}/><circle r="12" fill="#FFFFFF" {st(4)}/></g>'
# étoile de mer + coquillage
b+=f'<path transform="translate(560,1010) rotate(-12)" d="M0,-46 L13,-14 L46,-12 L20,9 L29,42 L0,23 L-29,42 L-20,9 L-46,-12 L-13,-14 Z" fill="#FF8A4C" {st(6)}/>'
b+=f'<path transform="translate(820,960)" d="M-34,20 Q-40,-30 0,-34 Q40,-30 34,20 Q0,34 -34,20 Z" fill="#FFB3C7" {st(6)}/><path transform="translate(820,960)" d="M0,26 L0,-30 M-16,24 L-12,-28 M16,24 L12,-28" fill="none" {st(4)}/>'
S['plage']=svg(d,b)

# ---------------------------------------------------------------- 2. VILLE LA NUIT
d=lg('sky',[(0,'#140F3D'),(.6,'#3A237A'),(1,'#7A3E9E')])+rg('moonglow',[(0,'#FFF6C9',.55),(1,'#FFF6C9',0)])+lg('road',[(0,'#3B3560'),(1,'#25204A')])+rg('lamp',[(0,'#FFE38A',.85),(1,'#FFE38A',0)])
b=f'<rect width="{W}" height="{H}" fill="url(#sky)"/>'+stars(170,7,0,0,W,620)
b+=f'<circle cx="380" cy="230" r="260" fill="url(#moonglow)"/><circle cx="380" cy="230" r="130" fill="#FFF3C4" {st(8)}/>'+''.join(f'<circle cx="{380+dx}" cy="{230+dy}" r="{rr}" fill="#F1DFA0" {st(4)}/>' for dx,dy,rr in [(-40,-30,24),(35,20,30),(-20,55,14)])
r=random.Random(11);x=-30
while x<W:  # silhouettes lointaines
    w=r.randint(90,170);h=r.randint(180,380);b+=f'<rect x="{x}" y="{760-h}" width="{w}" height="{h+20}" fill="#2C1F5E"/>';x+=w-6
r=random.Random(5);x=-40;cols=['#4B3A8C','#5A3E99','#3E3280','#6A4AA8']
while x<W:
    w=r.randint(150,250);h=r.randint(260,520);c=r.choice(cols)
    b+=f'<rect x="{x}" y="{790-h}" width="{w}" height="{h+30}" rx="6" fill="{c}" {st(7)}/>'
    if r.random()<.5: b+=f'<rect x="{x+w*.3}" y="{790-h-40}" width="{w*.4}" height="44" fill="{c}" {st(6)}/>'
    for wy in range(int(790-h+30),770,58):
        for wx in range(int(x+22),int(x+w-40),48):
            on=r.random()<.55
            b+=f'<rect x="{wx}" y="{wy}" width="26" height="34" rx="4" fill="{"#FFD45E" if on else "#2A2155"}" {st(4)}/>'
    x+=w+r.randint(-4,18)
b+=f'<rect x="-20" y="790" width="{W+40}" height="70" fill="#8C84B8" {st(7)}/><rect x="-20" y="860" width="{W+40}" height="240" fill="url(#road)" {st(7)}/>'
b+=''.join(f'<rect x="{x}" y="955" width="140" height="18" rx="9" fill="#FFD43B" opacity=".85"/>' for x in range(40,W,300))
for lx in [520,1420]:
    b+=f'<circle cx="{lx}" cy="560" r="170" fill="url(#lamp)"/><path d="M{lx},850 L{lx},560 Q{lx},520 {lx+40},520" fill="none" stroke="#2B2245" stroke-width="22" stroke-linecap="round"/><path d="M{lx},850 L{lx},560 Q{lx},520 {lx+40},520" fill="none" stroke="#5B5390" stroke-width="10" stroke-linecap="round"/>'
    b+=f'<path d="M{lx+10},515 L{lx+70},515 L{lx+60},560 L{lx+20},560 Z" fill="#FFE38A" {st(6)}/><rect x="{lx-22}" y="830" width="44" height="26" rx="6" fill="#5B5390" {st(5)}/>'
S['nuit']=svg(d,b)

# ---------------------------------------------------------------- 3. BATEAU PIRATE
d=lg('sky',[(0,'#57C2F7'),(.7,'#B5EBFF'),(1,'#E8FBFF')])+lg('sea',[(0,'#1E9FD6'),(1,'#0B6FA8')])+lg('deck',[(0,'#C9874C'),(1,'#9A5E2E')])+lg('sail',[(0,'#FFF8E6'),(1,'#EAD9B5')],0,0,1,0)
b=f'<rect width="{W}" height="{H}" fill="url(#sky)"/>'+cloud(1500,170,.9)+cloud(980,260,.6)+cloud(1780,330,.5)
b+=''.join(f'<path d="M{x},{y} q18,-16 36,0 q18,-16 36,0" fill="none" {st(6)}/>' for x,y in [(1200,170),(1290,120),(860,150)])
b+=f'<path d="M-20,520 L{W+20},520 L{W+20},800 L-20,800 Z" fill="url(#sea)" {st(7)}/>'
b+=f'<path d="M1500,520 q40,-60 110,-55 q70,4 100,55 Z" fill="#5CC46E" {st(6)}/>'
for i,y in enumerate([560,610,670]):
    b+=''.join(f'<path d="M{x},{y} q30,-16 60,0 q30,16 60,0" fill="none" stroke="#FFFFFF" stroke-width="7" stroke-linecap="round" opacity=".7"/>' for x in range(-40+(i%2)*120,W,320))
# mât + voile + drapeau
b+=f'<rect x="300" y="-20" width="58" height="840" fill="#8A5229" {st(7)}/><rect x="180" y="120" width="300" height="26" rx="10" fill="#8A5229" {st(6)}/><rect x="190" y="560" width="280" height="24" rx="10" fill="#8A5229" {st(6)}/>'
b+=f'<path d="M200,146 Q130,350 210,560 L450,560 Q530,350 460,146 Z" fill="url(#sail)" {st(7)}/><path d="M330,146 L330,560" stroke="#D8C49A" stroke-width="6"/>'
b+=f'<path d="M358,-10 L560,20 Q520,60 560,100 L358,90 Z" fill="#2B2245" {st(6)}/><g transform="translate(440,48)" fill="#FFFFFF"><circle r="20"/><rect x="-12" y="12" width="24" height="12" rx="4"/><circle cx="-7" cy="-2" r="5" fill="#2B2245"/><circle cx="7" cy="-2" r="5" fill="#2B2245"/><path d="M-30,30 L30,-26 M-30,-26 L30,30" stroke="#FFFFFF" stroke-width="8" stroke-linecap="round"/></g>'
# bastingage
b+=f'<rect x="-20" y="640" width="{W+40}" height="34" rx="10" fill="#B87437" {st(7)}/>'
b+=''.join(f'<path d="M{x-14},674 Q{x-22},720 {x-12},770 L{x+12},770 Q{x+22},720 {x+14},674 Z" fill="#C98A4B" {st(5)}/>' for x in range(30,W,90))
b+=f'<rect x="-20" y="766" width="{W+40}" height="30" fill="#8A5229" {st(7)}/>'
# pont en perspective
b+=f'<path d="M-20,796 L{W+20},796 L{W+20},{H+20} L-20,{H+20} Z" fill="url(#deck)" {st(7)}/>'
for i in range(-10,24):
    x0=W/2+i*95;x1=W/2+i*230
    b+=f'<path d="M{x0},796 L{x1},{H}" stroke="#7E4A22" stroke-width="5"/>'
b+=''.join(f'<path d="M-20,{y} L{W+20},{y}" stroke="#7E4A22" stroke-width="3" opacity=".5"/>' for y in [850,920,1005])
# tonneaux, corde, coffre
def barrel(x,y,s=1):
    return f'<g transform="translate({x},{y}) scale({s})"><path d="M-70,-150 Q-95,-75 -70,0 L70,0 Q95,-75 70,-150 Z" fill="#B87437" {st(7)}/><path d="M-82,-110 L82,-110 M-82,-40 L82,-40" stroke="#5E5A73" stroke-width="16"/><path d="M-82,-110 L82,-110 M-82,-40 L82,-40" {st(5)} fill="none"/><path d="M-30,-148 Q-40,-75 -30,0 M30,-148 Q40,-75 30,0" fill="none" stroke="#8A5229" stroke-width="5"/></g>'
b+=barrel(1660,1010)+barrel(1790,980,.85)
b+=f'<g transform="translate(1270,1000)"><rect x="-110" y="-90" width="220" height="90" rx="10" fill="#9A5E2E" {st(7)}/><path d="M-110,-90 Q-110,-170 0,-170 Q110,-170 110,-90 Z" fill="#B87437" {st(7)}/><rect x="-110" y="-100" width="220" height="20" fill="#FFD43B" {st(5)}/><rect x="-18" y="-112" width="36" height="44" rx="6" fill="#FFD43B" {st(5)}/><path d="M-60,-140 L-50,-150 M40,-150 L56,-138" stroke="#FFF3A0" stroke-width="8" stroke-linecap="round"/></g>'
b+=f'<g transform="translate(560,1010)"><ellipse rx="120" ry="40" fill="#E2C38A" {st(6)}/><ellipse rx="80" ry="24" fill="none" {st(5)}/><ellipse rx="40" ry="12" fill="#C9A86A" {st(5)}/></g>'
S['pirate']=svg(d,b)

# ---------------------------------------------------------------- 4. SOUS LA MER
d=lg('w',[(0,'#3ED0EE'),(.55,'#1488C6'),(1,'#0B4C8C')])+lg('sand',[(0,'#F5D891'),(1,'#D9B46A')])+lg('ray',[(0,'#FFFFFF'),(1,'#FFFFFF')])
b=f'<rect width="{W}" height="{H}" fill="url(#w)"/>'
b+=''.join(f'<path d="M{x},-20 L{x+90},-20 L{x+260},{H} L{x+100},{H} Z" fill="#FFFFFF" opacity=".09"/>' for x in [120,520,980,1420])
r=random.Random(8)
b+=''.join(f'<circle cx="{r.uniform(0,W):.0f}" cy="{r.uniform(60,800):.0f}" r="{r.choice([8,10,14,18])}" fill="#BFF4FF" fill-opacity=".25" stroke="#E6FBFF" stroke-width="4" opacity=".85"/>' for _ in range(40))
b+=f'<path d="M-20,620 Q300,560 640,610 T1280,600 T{W+20},590 L{W+20},{H} L-20,{H} Z" fill="#2E6FA8" opacity=".7"/>'
b+=f'<path d="M-20,800 Q420,740 860,790 T1600,770 T{W+20},780 L{W+20},{H+20} L-20,{H+20} Z" fill="url(#sand)" {st(7)}/>'
b+=''.join(f'<circle cx="{r.uniform(0,W):.0f}" cy="{r.uniform(850,1070):.0f}" r="5" fill="#B48A44" opacity=".5"/>' for _ in range(90))
def seaweed(x,y,h,c='#3FBF5A'):
    pts=' '.join(f'{x+math.sin(i*.9)*28:.0f},{y-i*h/8:.0f}' for i in range(9))
    return f'<polyline points="{pts}" fill="none" stroke="{O}" stroke-width="34" stroke-linecap="round" stroke-linejoin="round"/><polyline points="{pts}" fill="none" stroke="{c}" stroke-width="22" stroke-linecap="round" stroke-linejoin="round"/>'
b+=seaweed(110,1000,520)+seaweed(190,1010,380,'#2FA84C')+seaweed(1820,990,480)+seaweed(1730,1000,330,'#2FA84C')
def coral(x,y,s,c):
    return f'<g transform="translate({x},{y}) scale({s})" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M0,0 L0,-120 M0,-70 L-60,-140 M-60,-140 L-70,-200 M-60,-140 L-110,-170 M0,-120 L50,-190 M50,-190 L40,-240 M50,-190 L100,-220 M0,-60 L70,-110" stroke="{O}" stroke-width="46"/><path d="M0,0 L0,-120 M0,-70 L-60,-140 M-60,-140 L-70,-200 M-60,-140 L-110,-170 M0,-120 L50,-190 M50,-190 L40,-240 M50,-190 L100,-220 M0,-60 L70,-110" stroke="{c}" stroke-width="32"/></g>'
b+=coral(420,1000,1.2,'#FF6F91')+coral(1500,995,1.4,'#FF9F43')+coral(1620,1020,.8,'#C77DFF')
b+=f'<path d="M640,1000 Q630,920 720,910 Q800,880 860,930 Q930,940 920,1010 Z" fill="#8A84A8" {st(7)}/><path d="M1000,1010 Q990,960 1060,955 Q1120,950 1130,1012 Z" fill="#9F99BC" {st(6)}/>'
b+=f'<path transform="translate(1180,1015) rotate(10)" d="M0,-40 L12,-12 L40,-10 L18,8 L25,38 L0,20 L-25,38 L-18,8 L-40,-10 L-12,-12 Z" fill="#FFD43B" {st(6)}/>'
def fish(x,y,s,c,flip=1):
    return f'<g transform="translate({x},{y}) scale({s*flip},{s})"><path d="M-70,0 Q-30,-46 30,-30 Q70,-18 80,0 Q70,18 30,30 Q-30,46 -70,0 Z" fill="{c}" {st(6)}/><path d="M-66,0 L-120,-38 L-108,0 L-120,38 Z" fill="{c}" {st(6)}/><circle cx="44" cy="-6" r="10" fill="#FFFFFF" {st(4)}/><circle cx="47" cy="-6" r="4" fill="{O}"/><path d="M-10,-34 Q0,0 -10,34" fill="none" stroke="#FFFFFF" stroke-width="8" opacity=".8"/></g>'
b+=fish(1240,300,1,'#FFB703',-1)+fish(1330,380,.65,'#FF6F91',-1)+fish(560,240,.8,'#8DE08A')+fish(700,420,.55,'#C77DFF')
S['ocean']=svg(d,b)

# ---------------------------------------------------------------- 5. ESPACE
d=lg('sp',[(0,'#0D0828'),(1,'#2A1760')])+lg('gr',[(0,'#C9C2E6'),(1,'#9A90C4')])+lg('pl',[(0,'#FFB36B'),(1,'#E8574A')],0,0,1,1)+lg('pl2',[(0,'#7FE3FF'),(1,'#3B7BFF')],0,0,1,1)
b=f'<rect width="{W}" height="{H}" fill="url(#sp)"/>'
b+=f'<g filter="url(#blur40)" opacity=".55"><ellipse cx="520" cy="300" rx="420" ry="200" fill="#B154D8"/><ellipse cx="1300" cy="200" rx="380" ry="160" fill="#3A6BFF"/><ellipse cx="900" cy="420" rx="300" ry="120" fill="#FF6FB1"/></g>'
b+=stars(240,21,0,0,W,780)
b+=f'<g transform="translate(1450,330)"><ellipse rx="300" ry="60" fill="none" stroke="#FFE7B0" stroke-width="26" transform="rotate(-14)"/><circle r="170" fill="url(#pl)" {st(8)}/><path d="M-160,-40 Q0,-10 165,-60 M-150,60 Q0,90 150,40" fill="none" stroke="#C9452F" stroke-width="22" opacity=".55"/><path d="M-300,72 A300,60 0 0 0 290,-80" transform="rotate(-14)" fill="none" stroke="#FFE7B0" stroke-width="26"/></g>'
b+=f'<circle cx="380" cy="230" r="80" fill="url(#pl2)" {st(7)}/><path d="M330,200 q30,-20 60,0 q20,20 50,10 M320,260 q40,10 80,-10" fill="none" stroke="#FFFFFF" stroke-width="10" stroke-linecap="round" opacity=".6"/>'
b+=f'<g transform="translate(900,170) rotate(-30)"><path d="M0,0 L-160,0" stroke="#FFFFFF" stroke-width="6" opacity=".6" stroke-linecap="round"/><circle r="10" fill="#FFF6C9"/></g>'
b+=f'<path d="M-20,800 Q300,740 700,780 T1400,760 T{W+20},770 L{W+20},{H+20} L-20,{H+20} Z" fill="url(#gr)" {st(7)}/>'
for cx,cy,rx in [(300,930,110),(820,1010,70),(1180,880,60),(1560,980,130),(560,850,40)]:
    b+=f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{rx*.32}" fill="#8A80B6" {st(6)}/><ellipse cx="{cx}" cy="{cy+rx*.06}" rx="{rx*.75}" ry="{rx*.2}" fill="#7A70A8"/>'
# fusée
b+=f'''<g transform="translate(1720,840) rotate(8)"><path d="M0,-330 Q70,-250 70,-110 L70,20 L-70,20 L-70,-110 Q-70,-250 0,-330 Z" fill="#FFFFFF" {st(8)}/>
<path d="M0,-330 Q45,-290 60,-240 L-60,-240 Q-45,-290 0,-330 Z" fill="#FF4D4D" {st(6)}/><circle cy="-150" r="36" fill="#7FE3FF" {st(7)}/><circle cx="-10" cy="-160" r="10" fill="#FFFFFF"/>
<path d="M-70,-40 L-130,40 L-70,20 Z M70,-40 L130,40 L70,20 Z" fill="#FF4D4D" {st(7)}/><path d="M-40,20 L40,20 L26,60 L-26,60 Z" fill="#8A80B6" {st(6)}/></g>'''
S['espace']=svg(d,b)

# ---------------------------------------------------------------- 6. JUNGLE
d=lg('sky',[(0,'#9FE7C9'),(1,'#E9FFF2')])+lg('wf',[(0,'#BFF4FF'),(1,'#5FD0F0')],0,0,1,0)+lg('ground',[(0,'#7BC24A'),(1,'#4E9A34')])
b=f'<rect width="{W}" height="{H}" fill="url(#sky)"/>'
b+=hill(520,60,'#7FD19A',4)+hill(620,50,'#4FB878',9)
b+=f'<path d="M820,250 Q900,230 980,250 L1010,780 L790,780 Z" fill="#6E6A8E" {st(7)}/><path d="M850,255 Q900,245 950,255 L975,780 L825,780 Z" fill="url(#wf)" {st(6)}/>'
b+=''.join(f'<path d="M{x},{y} l0,90" stroke="#FFFFFF" stroke-width="8" stroke-linecap="round" opacity=".85"/>' for x,y in [(870,300),(910,420),(940,330),(880,560),(930,620)])
b+=f'<ellipse cx="900" cy="790" rx="190" ry="40" fill="#BFF4FF" {st(6)}/>'
b+=f'<path d="M-20,790 Q500,740 960,790 T{W+20},780 L{W+20},{H+20} L-20,{H+20} Z" fill="url(#ground)" {st(7)}/><path d="M640,{H} C760,980 980,960 900,880 C850,830 900,805 905,795 L945,795 C960,815 990,840 1010,880 C1090,960 1010,1010 1240,{H} Z" fill="#D9B46A" {st(6)}/>'
def leaf(x,y,ang,s,c='#2FA84C'):
    return f'<g transform="translate({x},{y}) rotate({ang}) scale({s})"><path d="M0,0 Q120,-90 300,-10 Q140,80 0,0 Z" fill="{c}" {st(7)}/><path d="M10,0 Q150,-20 290,-10" fill="none" stroke="#1E7E3A" stroke-width="6"/>'+''.join(f'<path d="M{60+i*45},{-5-i} l30,-40 M{60+i*45},{-5-i} l30,36" stroke="#1E7E3A" stroke-width="5" fill="none"/>' for i in range(5))+'</g>'
for x,y,a,s,c in [(-40,240,20,1.4,'#2FA84C'),(-60,520,-10,1.6,'#3FBF5A'),(-30,820,-30,1.3,'#2FA84C'),(W+40,300,160,1.5,'#3FBF5A'),(W+40,600,195,1.6,'#2FA84C'),(W+30,880,210,1.2,'#3FBF5A'),(380,-40,70,1.1,'#3FBF5A'),(1480,-40,110,1.2,'#2FA84C')]:
    b+=leaf(x,y,a,s,c)
b+=''.join(f'<g transform="translate({x},{y}) scale({s})"><circle cx="-70" cy="-40" r="70" fill="#3E9E4E" {st(7)}/><circle cx="40" cy="-70" r="85" fill="#4FB45E" {st(7)}/><circle cx="130" cy="-30" r="60" fill="#3E9E4E" {st(7)}/><rect x="-140" y="-30" width="330" height="40" fill="#3E9E4E"/><circle cx="20" cy="-100" r="22" fill="#7FE08A"/></g>' for x,y,s in [(330,830,1),(1500,820,1.1),(1180,800,.6),(640,810,.55)])
b+=''.join(f'<path d="M{x},-10 Q{x+30},{h*.5} {x},{h}" fill="none" stroke="{O}" stroke-width="16" stroke-linecap="round"/><path d="M{x},-10 Q{x+30},{h*.5} {x},{h}" fill="none" stroke="#6BAE3A" stroke-width="8" stroke-linecap="round"/>' for x,h in [(620,380),(1220,300),(1340,450)])
for x,y,c in [(420,960,'#FF6F91'),(1500,950,'#FFB703'),(1640,1010,'#FF6F91'),(300,1030,'#C77DFF')]:
    b+=f'<g transform="translate({x},{y})">'+''.join(f'<ellipse cx="{math.cos(math.radians(a))*22:.0f}" cy="{math.sin(math.radians(a))*22:.0f}" rx="20" ry="14" transform="rotate({a} {math.cos(math.radians(a))*22:.0f} {math.sin(math.radians(a))*22:.0f})" fill="{c}" {st(5)}/>' for a in range(0,360,72))+f'<circle r="12" fill="#FFE36B" {st(5)}/></g>'
S['jungle']=svg(d,b)

# ---------------------------------------------------------------- 7. CHÂTEAU
d=lg('sky',[(0,'#6CC8FF'),(1,'#D9F3FF')])+lg('stone',[(0,'#D7D2EA'),(1,'#B3ACD2')])
b=f'<rect width="{W}" height="{H}" fill="url(#sky)"/>'+cloud(330,200,.9)+cloud(1580,160,1)+cloud(1100,110,.55)
b+=hill(600,40,'#9EDB8A',2)
def tower(x,y,w,h,roof='#FF5A5A'):
    t=f'<rect x="{x-w/2}" y="{y-h}" width="{w}" height="{h}" fill="url(#stone)" {st(7)}/>'
    t+=f'<path d="M{x-w/2-14},{y-h} L{x},{y-h-w*1.1} L{x+w/2+14},{y-h} Z" fill="{roof}" {st(7)}/>'
    t+=f'<path d="M{x},{y-h-w*1.1} L{x},{y-h-w*1.1-70}" {st(6)}/><path d="M{x},{y-h-w*1.1-70} L{x+60},{y-h-w*1.1-55} L{x},{y-h-w*1.1-38} Z" fill="#FFD43B" {st(5)}/>'
    t+=f'<path d="M{x-12},{y-h+60} q12,-20 24,0 L{x+12},{y-h+110} L{x-12},{y-h+110} Z" fill="{O}"/>'
    return t
b+=tower(600,760,150,420)+tower(1320,760,150,420)
b+=f'<rect x="660" y="430" width="600" height="330" fill="url(#stone)" {st(7)}/>'
b+=''.join(f'<rect x="{x}" y="398" width="46" height="40" fill="url(#stone)" {st(6)}/>' for x in range(668,1250,90))
b+=tower(960,560,190,300,'#3BA7FF')
b+=f'<path d="M880,760 L880,640 Q960,560 1040,640 L1040,760 Z" fill="#8A5229" {st(7)}/>'+''.join(f'<path d="M{x},640 L{x},760" stroke="#5E3A1C" stroke-width="5"/>' for x in [920,960,1000])
b+=''.join(f'<path d="M{x},520 l0,30" stroke="{O}" stroke-width="14" stroke-linecap="round"/>' for x in [740,810,1110,1180])
for i in range(12):
    yy=470+(i%3)*60;xx=690+(i//3)*150
    b+=f'<path d="M{xx},{yy} l40,0" stroke="#9C95C0" stroke-width="4"/>'
b+=f'<path d="M-20,760 Q500,720 960,760 T{W+20},750 L{W+20},{H+20} L-20,{H+20} Z" fill="#6FCB5A" {st(7)}/>'
b+=f'<path d="M820,{H} Q900,900 900,760 L1020,760 Q1020,900 1100,{H} Z" fill="#E8D3A2" {st(6)}/>'
def tree(x,y,s=1):
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-18" y="-120" width="36" height="120" fill="#8A5229" {st(6)}/><circle cx="0" cy="-190" r="100" fill="#3FBF5A" {st(7)}/><circle cx="-70" cy="-140" r="60" fill="#3FBF5A" {st(7)}/><circle cx="70" cy="-140" r="60" fill="#3FBF5A" {st(7)}/><circle cx="-30" cy="-210" r="26" fill="#7FE08A"/><circle cx="-60" cy="-120" r="10" fill="#FF5A5A" {st(3)}/><circle cx="40" cy="-160" r="10" fill="#FF5A5A" {st(3)}/></g>'
b+=tree(220,1000,1.25)+tree(1720,990,1.15)+tree(420,860,.6)+tree(1520,850,.55)
for x,y,c in [(620,980,'#FF6F91'),(700,1040,'#FFD43B'),(1240,1000,'#FFFFFF'),(1330,1050,'#FF6F91')]:
    b+=f'<circle cx="{x}" cy="{y}" r="14" fill="{c}" {st(4)}/><circle cx="{x}" cy="{y}" r="5" fill="#FFB703"/>'
S['chateau']=svg(d,b)

# ---------------------------------------------------------------- 8. VOLCAN
d=lg('sky',[(0,'#3A1E4F'),(.5,'#C2453B'),(1,'#FF9A4A')])+lg('lava',[(0,'#FFE36B'),(1,'#FF5A1F')])+lg('rock',[(0,'#4A3B57'),(1,'#2D2338')])
b=f'<rect width="{W}" height="{H}" fill="url(#sky)"/>'
b+=f'<g filter="url(#blur12)" opacity=".75">'+''.join(f'<circle cx="{960+dx}" cy="{170+dy}" r="{rr}" fill="#5E4A68"/>' for dx,dy,rr in [(-120,0,110),(0,-60,140),(130,-10,120),(260,-90,100),(-250,-80,90)])+'</g>'
b+=f'<path d="M420,790 L860,300 Q960,270 1060,300 L1500,790 Z" fill="#6A4E6E" {st(8)}/><path d="M860,300 Q960,330 1060,300 Q1000,282 960,282 Q920,282 860,300 Z" fill="#FF5A1F" {st(6)}/>'
b+=f'<path d="M925,300 Q900,420 960,520 Q1010,610 940,790 L1040,790 Q1080,620 1030,520 Q990,420 1000,300 Z" fill="url(#lava)" {st(6)}/>'
b+=f'<g filter="url(#glow)">'+''.join(f'<circle cx="{960+dx}" cy="{230+dy}" r="{rr}" fill="{c}" {st(5)}/>' for dx,dy,rr,c in [(0,-40,34,'#FFE36B'),(-80,-90,22,'#FF9A3C'),(90,-110,26,'#FFE36B'),(-30,-170,18,'#FF9A3C'),(40,-60,16,'#FFFFFF')])+'</g>'
b+=f'<path d="M-20,800 Q400,760 900,800 T{W+20},790 L{W+20},{H+20} L-20,{H+20} Z" fill="url(#rock)" {st(7)}/>'
b+=f'<path d="M-20,940 Q300,890 600,930 Q800,960 990,920 L1000,950 Q800,990 600,962 Q300,925 -20,975 Z" fill="url(#lava)" {st(6)}/>'
b+=f'<path d="M1300,{H} Q1360,950 1500,930 Q1700,900 {W+20},920 L{W+20},{H} Z" fill="url(#lava)" {st(6)}/>'
for x,y,s in [(220,850,1),(1640,840,1.2),(760,1030,.9),(1150,880,.7)]:
    b+=f'<path transform="translate({x},{y}) scale({s})" d="M-90,30 Q-100,-40 -30,-60 Q30,-90 80,-40 Q120,0 90,30 Z" fill="#5A4868" {st(7)}/>'
def fern(x,y,s=1):
    return f'<g transform="translate({x},{y}) scale({s})">'+''.join(f'<path d="M0,0 Q{dx*.5},{-120} {dx},{-200+abs(dx)*.4}" fill="none" stroke="{O}" stroke-width="22" stroke-linecap="round"/><path d="M0,0 Q{dx*.5},{-120} {dx},{-200+abs(dx)*.4}" fill="none" stroke="#3E8E4A" stroke-width="12" stroke-linecap="round"/>' for dx in [-160,-80,0,80,160])+'</g>'
b+=fern(90,1060,1.3)+fern(1830,1060,1.2)
S['volcan']=svg(d,b)

# ---------------------------------------------------------------- 9. FAR WEST
d=lg('sky',[(0,'#FF9E5E'),(.6,'#FFD08A'),(1,'#FFE9B8')])+lg('sand',[(0,'#F2B266'),(1,'#D98C42')])+lg('mesa',[(0,'#D8643A'),(1,'#B2462B')])
b=f'<rect width="{W}" height="{H}" fill="url(#sky)"/><circle cx="960" cy="560" r="230" fill="#FFE36B" {st(8)}/><circle cx="960" cy="560" r="300" fill="#FFF3A6" opacity=".25"/>'
b+=f'<path d="M-20,640 L120,640 L160,420 L520,420 L560,640 L1320,640 L1370,470 L1700,470 L1740,640 L{W+20},640 L{W+20},800 L-20,800 Z" fill="url(#mesa)" {st(7)}/>'
b+=''.join(f'<path d="M{x0},{y} L{x1},{y}" stroke="#9E3A22" stroke-width="6" opacity=".6"/>' for x0,x1,y in [(170,510,480),(150,530,560),(1380,1690,530),(1360,1720,590)])
b+=f'<path d="M-20,780 Q500,740 960,780 T{W+20},770 L{W+20},{H+20} L-20,{H+20} Z" fill="url(#sand)" {st(7)}/>'
def cactus(x,y,s=1):
    g='#3FA35A'
    return f'''<g transform="translate({x},{y}) scale({s})"><path d="M-40,0 L-40,-380 Q-40,-430 0,-430 Q40,-430 40,-380 L40,0 Z" fill="{g}" {st(7)}/>
<path d="M-40,-200 L-110,-200 Q-140,-200 -140,-240 L-140,-320 Q-140,-350 -112,-350 Q-86,-350 -86,-320 L-86,-250 L-40,-250 Z" fill="{g}" {st(7)}/>
<path d="M40,-150 L110,-150 Q140,-150 140,-190 L140,-290 Q140,-320 112,-320 Q86,-320 86,-290 L86,-200 L40,-200 Z" fill="{g}" {st(7)}/>
<path d="M0,-410 L0,-20 M-112,-335 L-112,-215 M112,-305 L112,-165" stroke="#2C8A47" stroke-width="6" fill="none"/><circle cx="0" cy="-440" r="14" fill="#FF6F91" {st(4)}/></g>'''
b+=cactus(260,1010,1.15)+cactus(1680,960,.9)+cactus(680,800,.35)
# façade saloon
b+=f'<g transform="translate(1290,1000)"><rect x="-200" y="-330" width="400" height="330" fill="#B87437" {st(7)}/><path d="M-230,-330 L230,-330 L230,-420 L140,-420 L140,-450 L-140,-450 L-140,-420 L-230,-420 Z" fill="#C98A4B" {st(7)}/>'+''.join(f'<path d="M-200,{-310+i*40} L200,{-310+i*40}" stroke="#8A5229" stroke-width="4"/>' for i in range(8))+'<rect x="-60" y="-190" width="120" height="190" fill="#5E3A1C" stroke="#2B2245" stroke-width="7"/><path d="M-60,-150 L-2,-150 L-2,-50 L-60,-50 Z M2,-150 L60,-150 L60,-50 L2,-50 Z" fill="#C98A4B" stroke="#2B2245" stroke-width="6"/><rect x="-170" y="-260" width="80" height="70" fill="#FFE36B" stroke="#2B2245" stroke-width="6"/><rect x="90" y="-260" width="80" height="70" fill="#FFE36B" stroke="#2B2245" stroke-width="6"/><rect x="-110" y="-410" width="220" height="56" rx="8" fill="#FFF3D6" stroke="#2B2245" stroke-width="6"/><path d="M-80,-382 L80,-382" stroke="#B2462B" stroke-width="10" stroke-linecap="round"/></g>'
b+=f'<g transform="translate(560,1000)"><circle r="56" fill="none" stroke="#B88A4A" stroke-width="10"/><path d="M-40,-30 Q0,10 40,-30 M-50,10 Q0,-30 50,20 M-20,-50 Q10,0 -10,50 M20,-50 Q-10,0 30,46" fill="none" stroke="#B88A4A" stroke-width="8"/></g>'
S['farwest']=svg(d,b)

# ---------------------------------------------------------------- 10. MONTAGNE
d=lg('sky',[(0,'#7CC7FF'),(1,'#E4F4FF')])+lg('mt',[(0,'#9FB0E0'),(1,'#7A8CC4')])+lg('snow',[(0,'#FFFFFF'),(1,'#DCEBFF')])
b=f'<rect width="{W}" height="{H}" fill="url(#sky)"/>'+cloud(1500,180,.8)+cloud(420,140,.6)
for x,h,c in [(380,520,'#8FA2D8'),(1000,640,'#7A8CC4'),(1600,500,'#8FA2D8')]:
    b+=f'<path d="M{x-420},790 L{x},{790-h} L{x+420},790 Z" fill="{c}" {st(8)}/><path d="M{x-150},{790-h+180} L{x},{790-h} L{x+150},{790-h+180} q-30,30 -60,0 q-30,30 -60,0 q-30,30 -60,0 q-30,30 -30,0 z" fill="#FFFFFF" {st(6)}/>'
b+=f'<path d="M-20,770 Q500,720 960,770 T{W+20},760 L{W+20},{H+20} L-20,{H+20} Z" fill="url(#snow)" {st(7)}/>'
b+=''.join(pine(x,y,h,'#2E8B57',True) for x,y,h in [(120,960,420),(280,860,260),(1820,980,440),(1660,880,280),(620,800,170),(1360,790,150)])
# chalet
b+=f'''<g transform="translate(1180,940)"><rect x="-170" y="-200" width="340" height="200" fill="#B87437" {st(7)}/>{''.join(f'<path d="M-170,{-180+i*36} L170,{-180+i*36}" stroke="#8A5229" stroke-width="5"/>' for i in range(5))}
<path d="M-220,-190 L0,-360 L220,-190 Z" fill="#8A5229" {st(7)}/><path d="M-235,-185 L0,-372 L235,-185 q-40,24 -80,0 q-40,24 -80,0 q-40,24 -80,0 q-40,24 -80,0 q-40,24 -80,0 q-30,20 -70,0 z" fill="#FFFFFF" {st(6)}/>
<rect x="-120" y="-140" width="80" height="70" fill="#FFD45E" {st(6)}/><path d="M-80,-140 L-80,-70 M-120,-105 L-40,-105" {st(5)}/><rect x="40" y="-120" width="80" height="120" fill="#5E3A1C" {st(6)}/><circle cx="104" cy="-60" r="6" fill="#FFD43B"/>
<rect x="90" y="-330" width="50" height="90" fill="#8A84A8" {st(6)}/></g>'''
b+=f'<g transform="translate(700,1000)"><circle cy="-60" r="70" fill="#FFFFFF" {st(7)}/><circle cy="-170" r="50" fill="#FFFFFF" {st(7)}/><circle cx="-16" cy="-180" r="7" fill="{O}"/><circle cx="16" cy="-180" r="7" fill="{O}"/><path d="M0,-166 L44,-158 L0,-150 Z" fill="#FF9F43" {st(4)}/><path d="M-50,-128 Q0,-110 50,-128 L46,-112 Q0,-96 -46,-112 Z" fill="#FF4D4D" {st(5)}/><circle cy="-70" r="7" fill="{O}"/><circle cy="-40" r="7" fill="{O}"/></g>'
r=random.Random(31)
b+=''.join(f'<circle cx="{r.uniform(0,W):.0f}" cy="{r.uniform(0,760):.0f}" r="{r.choice([4,5,7])}" fill="#FFFFFF" opacity=".85"/>' for _ in range(70))
S['montagne']=svg(d,b)

# ---------------------------------------------------------------- 11. THÉÂTRE
d=lg('back',[(0,'#2A1758'),(1,'#4A2A84')])+lg('cur',[(0,'#E33A3A'),(.5,'#B8202A'),(1,'#E33A3A')],0,0,1,0)+lg('floor',[(0,'#C98A4B'),(1,'#8A5229')])+lg('beam',[(0,'#FFF3B0'),(1,'#FFF3B0')])
b=f'<rect width="{W}" height="{H}" fill="url(#back)"/>'+stars(60,44,300,160,1620,700,'#FFE9A6')
b+=''.join(f'<path d="M{x},120 L{x-260},800 L{x+260},800 Z" fill="#FFF3B0" opacity=".14"/>' for x in [620,1300])
b+=f'<path d="M-20,800 L{W+20},800 L{W+20},{H+20} L-20,{H+20} Z" fill="url(#floor)" {st(7)}/>'
b+=''.join(f'<path d="M{W/2+i*80},800 L{W/2+i*170},{H}" stroke="#7E4A22" stroke-width="4"/>' for i in range(-14,15))
b+=''.join(f'<ellipse cx="{x}" cy="800" rx="230" ry="40" fill="#FFF3B0" opacity=".25"/>' for x in [620,1300])
b+=f'<rect x="-20" y="790" width="{W+40}" height="24" fill="#5E3A1C" {st(6)}/>'
def curtain(x0,x1,side):
    folds=7;w=(x1-x0)/folds;out=''
    for i in range(folds):
        a=x0+i*w;out+=f'<path d="M{a},-20 L{a+w},-20 L{a+w+ (side*10)},{820} Q{a+w/2},{860} {a+(side*10)},{820} Z" fill="url(#cur)" {st(6)}/>'
    return out
b+=f'<g>{curtain(-60,330,1)}</g><path d="M330,-20 Q260,380 330,830" fill="none" stroke="#FFD43B" stroke-width="0"/>'
b+=f'<g>{curtain(1590,1980,-1)}</g>'
b+=f'<path d="M210,430 Q330,460 380,430" fill="none" stroke="#FFD43B" stroke-width="22" stroke-linecap="round"/><circle cx="380" cy="436" r="22" fill="#FFD43B" {st(5)}/><path d="M1710,430 Q1590,460 1540,430" fill="none" stroke="#FFD43B" stroke-width="22" stroke-linecap="round"/><circle cx="1540" cy="436" r="22" fill="#FFD43B" {st(5)}/>'
b+=f'<path d="M-20,-20 L{W+20},-20 L{W+20},150 '+''.join(f'Q{W-i*240-120},{230} {W-(i+1)*240},150 ' for i in range(8))+f'L-20,150 Z" fill="url(#cur)" {st(7)}/>'
b+=f'<path d="M-20,140 '+''.join(f'Q{i*240+120},{220} {(i+1)*240},140 ' for i in range(8))+'" fill="none" stroke="#FFD43B" stroke-width="16"/>'
b+=''.join(f'<g transform="translate({x},205)"><path d="M0,-30 L0,0" {st(5)}/><path d="M-14,0 L14,0 L20,50 L-20,50 Z" fill="#FFD43B" {st(5)}/></g>' for x in range(120,W,240))
b+=''.join(f'<path d="M{x-30},{H+10} L{x-20},{H-40} L{x+20},{H-40} L{x+30},{H+10} Z" fill="#3B3560" {st(5)}/><ellipse cx="{x}" cy="{H-44}" rx="18" ry="8" fill="#FFE36B"/>' for x in range(160,W,320))
S['theatre']=svg(d,b)

# ---------------------------------------------------------------- 12. MANOIR HANTÉ
d=lg('sky',[(0,'#1A1240'),(.65,'#3D2470'),(1,'#5E3A8C')])+rg('mg',[(0,'#E8FFC9',.5),(1,'#E8FFC9',0)])+lg('hill',[(0,'#3A2E5E'),(1,'#241C40')])
b=f'<rect width="{W}" height="{H}" fill="url(#sky)"/>'+stars(120,77,0,0,W,600)
b+=f'<circle cx="1420" cy="250" r="300" fill="url(#mg)"/><circle cx="1420" cy="250" r="160" fill="#F4FFD6" {st(8)}/>'+''.join(f'<circle cx="{1420+dx}" cy="{250+dy}" r="{rr}" fill="#DCEBB8" {st(4)}/>' for dx,dy,rr in [(-50,-40,26),(40,30,34),(-10,70,16)])
b+=''.join(f'<path transform="translate({x},{y}) scale({s})" d="M0,0 Q-20,-24 -46,-10 Q-60,-24 -80,-8 Q-56,-4 -50,16 Q-30,6 0,12 Q30,6 50,16 Q56,-4 80,-8 Q60,-24 46,-10 Q20,-24 0,0 Z" fill="{O}"/>' for x,y,s in [(1260,180,1),(1560,330,.7),(1100,300,.55),(700,160,.6)])
b+=f'<path d="M-20,700 Q500,560 1000,640 T{W+20},620 L{W+20},{H+20} L-20,{H+20} Z" fill="url(#hill)" {st(7)}/>'
# manoir
b+=f'''<g transform="translate(860,690)"><rect x="-260" y="-260" width="520" height="260" fill="#5B4A86" {st(7)}/><path d="M-300,-250 L0,-420 L300,-250 Z" fill="#3B2E64" {st(7)}/>
<rect x="160" y="-470" width="110" height="250" fill="#5B4A86" {st(7)}/><path d="M140,-470 L215,-570 L290,-470 Z" fill="#3B2E64" {st(7)}/>
<rect x="-60" y="-140" width="120" height="140" rx="60" fill="#2B2245" {st(6)}/>
{''.join(f'<rect x="{x}" y="{y}" width="70" height="80" rx="6" fill="#FFD45E" {st(6)}/><path d="M{x+35},{y} L{x+35},{y+80} M{x},{y+40} L{x+70},{y+40}" {st(4)}/>' for x,y in [(-220,-210),(-120,-210),(50,-210),(150,-210),(-220,-110),(150,-110),(180,-420)])}
<circle cx="0" cy="-320" r="34" fill="#FFD45E" {st(6)}/></g>'''
def bare_tree(x,y,s=1):
    return f'<g transform="translate({x},{y}) scale({s})" fill="none" stroke-linecap="round"><path d="M0,0 L0,-260 M0,-180 L-90,-260 M-90,-260 L-120,-320 M-90,-260 L-150,-270 M0,-260 L70,-340 M70,-340 L60,-400 M70,-340 L130,-360 M0,-120 L80,-170" stroke="{O}" stroke-width="40"/><path d="M0,0 L0,-260 M0,-180 L-90,-260 M-90,-260 L-120,-320 M-90,-260 L-150,-270 M0,-260 L70,-340 M70,-340 L60,-400 M70,-340 L130,-360 M0,-120 L80,-170" stroke="#4A3A6A" stroke-width="26"/></g>'
b+=bare_tree(230,1000,1.3)+bare_tree(1700,980,1.1)
b+=f'<path d="M-20,860 Q600,820 1100,860 T{W+20},850 L{W+20},{H+20} L-20,{H+20} Z" fill="#2B2350" {st(7)}/>'
for x,y,s in [(560,960,1),(720,1010,.8),(1300,990,1.1),(1460,940,.75)]:
    b+=f'<path transform="translate({x},{y}) scale({s})" d="M-50,0 L-50,-100 Q-50,-150 0,-150 Q50,-150 50,-100 L50,0 Z" fill="#8A84A8" {st(7)}/><path transform="translate({x},{y}) scale({s})" d="M-24,-90 L24,-90 M0,-112 L0,-60" stroke="#5E5A73" stroke-width="10" stroke-linecap="round"/>'
def pumpkin(x,y,s=1):
    return f'<g transform="translate({x},{y}) scale({s})"><ellipse rx="80" ry="62" fill="#FF8A2B" {st(7)}/><ellipse rx="34" ry="62" fill="none" {st(5)}/><path d="M0,-60 Q4,-90 24,-96" fill="none" stroke="#3E8E4A" stroke-width="14" stroke-linecap="round"/><path d="M-44,-14 L-24,-30 L-14,-8 Z M44,-14 L24,-30 L14,-8 Z" fill="#FFE36B" {st(4)}/><path d="M-40,20 Q0,46 40,20 Q20,30 0,26 Q-20,30 -40,20 Z" fill="#FFE36B" {st(4)}/></g>'
b+=pumpkin(980,1010)+pumpkin(1110,1040,.6)+pumpkin(400,1050,.7)
b+=''.join(f'<path d="M{x},{860+i*0} L{x},790" stroke="{O}" stroke-width="14" stroke-linecap="round"/><path d="M{x-8},795 L{x},775 L{x+8},795" fill="{O}"/>' for i,x in enumerate(range(20,W,70)) if not 700<x<1000)
b+=f'<path d="M-20,820 L{W+20},820" stroke="{O}" stroke-width="12"/>'
S['manoir']=svg(d,b)

if __name__=='__main__':
    import sys,os
    out=sys.argv[1]
    for k,v in S.items(): open(os.path.join(out,k+'.svg'),'w').write(v)
    print(len(S),'scènes')
