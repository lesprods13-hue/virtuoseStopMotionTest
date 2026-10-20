# Décors cartoon VERTICAUX 1080x1920 (films en portrait) — même style que decors.py :
# contours épais, couleurs franches, grand ciel en haut et sol en bas pour poser les personnages.
import random, math, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import decors as D
D.W, D.H = 1080, 1920                     # les fonctions svg(), hill()... lisent ces valeurs
W, H = D.W, D.H
O = D.O
from decors import lg, rg, st, cloud, stars, palm, pine
svg, hill = D.svg, D.hill

S = {}
# ---------------------------------------------------------------- 1. PLAGE
d=lg('sky',[(0,'#3FB6F2'),(.6,'#9FE3FF'),(1,'#D8F6FF')])+lg('sea',[(0,'#1FB5C9'),(1,'#0E8FB5')])+lg('sand',[(0,'#FFE29A'),(1,'#F7C565')])+rg('sun',[(0,'#FFF3A6',1),(.55,'#FFD84A',1),(1,'#FFD84A',0)])
b=f'<rect width="{W}" height="{H}" fill="url(#sky)"/>'
sx,sy=790,330
b+=f'<circle cx="{sx}" cy="{sy}" r="230" fill="url(#sun)" opacity=".6"/>'
b+=''.join(f'<path d="M{sx},{sy} L{sx+math.cos(math.radians(a))*260:.0f},{sy+math.sin(math.radians(a))*260:.0f}" stroke="#FFE36B" stroke-width="18" stroke-linecap="round" opacity=".7"/>' for a in range(0,360,30))
b+=f'<circle cx="{sx}" cy="{sy}" r="120" fill="#FFD84A" {st(8)}/><circle cx="{sx-35}" cy="{sy-30}" r="34" fill="#FFF1A0"/>'
b+=cloud(260,260,1)+cloud(560,620,.7)+cloud(900,820,.55)+cloud(200,940,.45)
b+=f'<path d="M-20,1120 L{W+20},1120 L{W+20},1380 L-20,1380 Z" fill="url(#sea)" {st(7)}/>'
b+=f'<path d="M640,1120 q60,-70 150,-60 q90,10 120,60 Z" fill="#5CC46E" {st(6)}/>'+palm(790,1120,120,1,.5)
for i,y in enumerate([1160,1205,1255,1305]):
    b+=''.join(f'<path d="M{x},{y} q30,-16 60,0 q30,16 60,0" fill="none" stroke="#FFFFFF" stroke-width="7" stroke-linecap="round" opacity=".75"/>' for x in range(-40+(i%2)*90,W,300))
b+=f'<path d="M-20,1370 Q240,1310 520,1350 T{W+20},1330 L{W+20},{H+20} L-20,{H+20} Z" fill="url(#sand)" {st(7)}/>'
b+=f'<path d="M-20,1370 Q240,1310 520,1350 T{W+20},1330" fill="none" stroke="#FFFFFF" stroke-width="16" stroke-linecap="round" opacity=".9" transform="translate(0,-12)"/>'
r=random.Random(3)
b+=''.join(f'<circle cx="{r.uniform(0,W):.0f}" cy="{r.uniform(1430,1910):.0f}" r="4" fill="#E2A94A" opacity=".6"/>' for _ in range(110))
b+=palm(120,1820,1000,1.0,1)
# parasol + serviette (repris du décor horizontal, déplacé à droite)
g=f'<path d="M1500,990 L1460,640" stroke="{O}" stroke-width="24" stroke-linecap="round"/><path d="M1500,990 L1460,640" stroke="#FFFFFF" stroke-width="12" stroke-linecap="round"/>'
g+=f'<path d="M1240,690 Q1300,520 1460,520 Q1620,520 1690,680 Q1640,650 1600,682 Q1550,640 1490,676 Q1420,640 1370,680 Q1310,650 1240,690 Z" fill="#FF5A5A" {st(7)}/>'
g+=f'<path d="M1370,680 Q1380,560 1460,520 Q1430,600 1490,676 M1600,682 Q1570,570 1460,520" fill="none" {st(6)}/><path d="M1390,620 Q1420,560 1460,525 Q1450,600 1480,660 Z M1570,640 Q1540,570 1462,524 Q1520,560 1600,682 Z" fill="#FFFFFF" opacity=".9"/>'
g+=f'<path d="M1300,960 L1700,935 L1745,1020 L1330,1050 Z" fill="#3BA7FF" {st(6)}/>'+''.join(f'<path d="M{1300+i*80+10},{958-i*5} L{1335+i*82+12},{1048-i*6}" stroke="#FFFFFF" stroke-width="14"/>' for i in range(5))
b+=f'<g transform="translate(-700,640)">{g}</g>'
b+=f'<g transform="translate(450,1800)"><circle r="58" fill="#FFFFFF" {st(6)}/><path d="M-58,0 A58,58 0 0 1 0,-58 L0,0 Z" fill="#FF5A5A"/><path d="M0,58 A58,58 0 0 1 -58,0 L0,0 Z" fill="#FFD43B"/><path d="M58,0 A58,58 0 0 1 0,58 L0,0Z" fill="#3BA7FF"/><circle r="58" fill="none" {st(6)}/><circle r="12" fill="#FFFFFF" {st(4)}/></g>'
b+=f'<path transform="translate(940,1850) rotate(-12)" d="M0,-46 L13,-14 L46,-12 L20,9 L29,42 L0,23 L-29,42 L-20,9 L-46,-12 L-13,-14 Z" fill="#FF8A4C" {st(6)}/>'
b+=f'<path transform="translate(300,1500)" d="M-34,20 Q-40,-30 0,-34 Q40,-30 34,20 Q0,34 -34,20 Z" fill="#FFB3C7" {st(6)}/><path transform="translate(300,1500)" d="M0,26 L0,-30 M-16,24 L-12,-28 M16,24 L12,-28" fill="none" {st(4)}/>'
S['plage']=svg(d,b)

# ---------------------------------------------------------------- 2. VILLE LA NUIT
d=lg('sky',[(0,'#140F3D'),(.6,'#3A237A'),(1,'#7A3E9E')])+rg('moonglow',[(0,'#FFF6C9',.55),(1,'#FFF6C9',0)])+lg('road',[(0,'#3B3560'),(1,'#25204A')])+rg('lamp',[(0,'#FFE38A',.85),(1,'#FFE38A',0)])
b=f'<rect width="{W}" height="{H}" fill="url(#sky)"/>'+stars(150,7,0,0,W,1000)
b+=f'<circle cx="300" cy="320" r="260" fill="url(#moonglow)"/><circle cx="300" cy="320" r="130" fill="#FFF3C4" {st(8)}/>'+''.join(f'<circle cx="{300+dx}" cy="{320+dy}" r="{rr}" fill="#F1DFA0" {st(4)}/>' for dx,dy,rr in [(-40,-30,24),(35,20,30),(-20,55,14)])
BASE=1390
r=random.Random(11);x=-30
while x<W:
    w=r.randint(90,160);h=r.randint(380,760);b+=f'<rect x="{x}" y="{BASE-30-h}" width="{w}" height="{h+20}" fill="#2C1F5E"/>';x+=w-6
r=random.Random(5);x=-40;cols=['#4B3A8C','#5A3E99','#3E3280','#6A4AA8']
while x<W:
    w=r.randint(160,240);h=r.randint(420,820);c=r.choice(cols)
    b+=f'<rect x="{x}" y="{BASE-h}" width="{w}" height="{h+30}" rx="6" fill="{c}" {st(7)}/>'
    if r.random()<.5: b+=f'<rect x="{x+w*.3}" y="{BASE-h-40}" width="{w*.4}" height="44" fill="{c}" {st(6)}/>'
    for wy in range(int(BASE-h+30),BASE-20,58):
        for wx in range(int(x+22),int(x+w-40),48):
            on=r.random()<.55
            b+=f'<rect x="{wx}" y="{wy}" width="26" height="34" rx="4" fill="{"#FFD45E" if on else "#2A2155"}" {st(4)}/>'
    x+=w+r.randint(-4,18)
b+=f'<rect x="-20" y="{BASE}" width="{W+40}" height="80" fill="#8C84B8" {st(7)}/><rect x="-20" y="{BASE+80}" width="{W+40}" height="{H-BASE}" fill="url(#road)" {st(7)}/>'
b+=''.join(f'<rect x="{x}" y="1680" width="140" height="18" rx="9" fill="#FFD43B" opacity=".85"/>' for x in range(40,W,300))
for lx in [150,830]:
    top=900
    b+=f'<circle cx="{lx}" cy="{top}" r="190" fill="url(#lamp)"/><path d="M{lx},{BASE+60} L{lx},{top} Q{lx},{top-40} {lx+40},{top-40}" fill="none" stroke="#2B2245" stroke-width="22" stroke-linecap="round"/><path d="M{lx},{BASE+60} L{lx},{top} Q{lx},{top-40} {lx+40},{top-40}" fill="none" stroke="#5B5390" stroke-width="10" stroke-linecap="round"/>'
    b+=f'<path d="M{lx+10},{top-45} L{lx+70},{top-45} L{lx+60},{top} L{lx+20},{top} Z" fill="#FFE38A" {st(6)}/><rect x="{lx-22}" y="{BASE+40}" width="44" height="26" rx="6" fill="#5B5390" {st(5)}/>'
S['nuit']=svg(d,b)

# ---------------------------------------------------------------- 3. BATEAU PIRATE
d=lg('sky',[(0,'#57C2F7'),(.7,'#B5EBFF'),(1,'#E8FBFF')])+lg('sea',[(0,'#1E9FD6'),(1,'#0B6FA8')])+lg('deck',[(0,'#C9874C'),(1,'#9A5E2E')])+lg('sail',[(0,'#FFF8E6'),(1,'#EAD9B5')],0,0,1,0)
b=f'<rect width="{W}" height="{H}" fill="url(#sky)"/>'+cloud(820,260,.9)+cloud(620,560,.6)+cloud(960,760,.5)
b+=''.join(f'<path d="M{x},{y} q18,-16 36,0 q18,-16 36,0" fill="none" {st(6)}/>' for x,y in [(560,240),(650,190),(720,420)])
b+=f'<path d="M-20,1120 L{W+20},1120 L{W+20},1410 L-20,1410 Z" fill="url(#sea)" {st(7)}/>'
b+=f'<path d="M760,1120 q40,-60 110,-55 q70,4 100,55 Z" fill="#5CC46E" {st(6)}/>'
for i,y in enumerate([1160,1210,1265]):
    b+=''.join(f'<path d="M{x},{y} q30,-16 60,0 q30,16 60,0" fill="none" stroke="#FFFFFF" stroke-width="7" stroke-linecap="round" opacity=".7"/>' for x in range(-40+(i%2)*120,W,320))
# mât + grande voile + drapeau
b+=f'<rect x="200" y="-20" width="58" height="1440" fill="#8A5229" {st(7)}/><rect x="80" y="230" width="300" height="26" rx="10" fill="#8A5229" {st(6)}/><rect x="90" y="990" width="280" height="24" rx="10" fill="#8A5229" {st(6)}/>'
b+=f'<path d="M100,256 Q20,620 110,990 L350,990 Q440,620 360,256 Z" fill="url(#sail)" {st(7)}/><path d="M230,256 L230,990" stroke="#D8C49A" stroke-width="6"/>'
b+=f'<path d="M258,30 L460,60 Q420,100 460,140 L258,130 Z" fill="#2B2245" {st(6)}/><g transform="translate(340,88)" fill="#FFFFFF"><circle r="20"/><rect x="-12" y="12" width="24" height="12" rx="4"/><circle cx="-7" cy="-2" r="5" fill="#2B2245"/><circle cx="7" cy="-2" r="5" fill="#2B2245"/><path d="M-30,30 L30,-26 M-30,-26 L30,30" stroke="#FFFFFF" stroke-width="8" stroke-linecap="round"/></g>'
# vigie
b+=f'<path d="M150,160 L310,160 L290,215 L170,215 Z" fill="#B87437" {st(6)}/>'
# bastingage
RY=1240
b+=f'<rect x="-20" y="{RY}" width="{W+40}" height="34" rx="10" fill="#B87437" {st(7)}/>'
b+=''.join(f'<path d="M{x-14},{RY+34} Q{x-22},{RY+80} {x-12},{RY+130} L{x+12},{RY+130} Q{x+22},{RY+80} {x+14},{RY+34} Z" fill="#C98A4B" {st(5)}/>' for x in range(30,W,90))
b+=f'<rect x="-20" y="{RY+126}" width="{W+40}" height="30" fill="#8A5229" {st(7)}/>'
DY=RY+156
b+=f'<path d="M-20,{DY} L{W+20},{DY} L{W+20},{H+20} L-20,{H+20} Z" fill="url(#deck)" {st(7)}/>'
for i in range(-10,12):
    x0=W/2+i*80;x1=W/2+i*210
    b+=f'<path d="M{x0},{DY} L{x1},{H}" stroke="#7E4A22" stroke-width="5"/>'
b+=''.join(f'<path d="M-20,{y} L{W+20},{y}" stroke="#7E4A22" stroke-width="3" opacity=".5"/>' for y in [1480,1590,1740])
def barrel(x,y,s=1):
    return f'<g transform="translate({x},{y}) scale({s})"><path d="M-70,-150 Q-95,-75 -70,0 L70,0 Q95,-75 70,-150 Z" fill="#B87437" {st(7)}/><path d="M-82,-110 L82,-110 M-82,-40 L82,-40" stroke="#5E5A73" stroke-width="16"/><path d="M-82,-110 L82,-110 M-82,-40 L82,-40" {st(5)} fill="none"/><path d="M-30,-148 Q-40,-75 -30,0 M30,-148 Q40,-75 30,0" fill="none" stroke="#8A5229" stroke-width="5"/></g>'
b+=barrel(860,1840)+barrel(990,1800,.85)
b+=f'<g transform="translate(560,1870) scale(.9)"><rect x="-110" y="-90" width="220" height="90" rx="10" fill="#9A5E2E" {st(7)}/><path d="M-110,-90 Q-110,-170 0,-170 Q110,-170 110,-90 Z" fill="#B87437" {st(7)}/><rect x="-110" y="-100" width="220" height="20" fill="#FFD43B" {st(5)}/><rect x="-18" y="-112" width="36" height="44" rx="6" fill="#FFD43B" {st(5)}/><path d="M-60,-140 L-50,-150 M40,-150 L56,-138" stroke="#FFF3A0" stroke-width="8" stroke-linecap="round"/></g>'
b+=f'<g transform="translate(190,1820)"><ellipse rx="120" ry="40" fill="#E2C38A" {st(6)}/><ellipse rx="80" ry="24" fill="none" {st(5)}/><ellipse rx="40" ry="12" fill="#C9A86A" {st(5)}/></g>'
S['pirate']=svg(d,b)

# ---------------------------------------------------------------- 4. SOUS LA MER
d=lg('w',[(0,'#3ED0EE'),(.55,'#1488C6'),(1,'#0B4C8C')])+lg('sand',[(0,'#F5D891'),(1,'#D9B46A')])
b=f'<rect width="{W}" height="{H}" fill="url(#w)"/>'
b+=''.join(f'<path d="M{x},-20 L{x+90},-20 L{x+360},{H} L{x+200},{H} Z" fill="#FFFFFF" opacity=".09"/>' for x in [40,380,720])
r=random.Random(8)
b+=''.join(f'<circle cx="{r.uniform(0,W):.0f}" cy="{r.uniform(60,1350):.0f}" r="{r.choice([8,10,14,18])}" fill="#BFF4FF" fill-opacity=".25" stroke="#E6FBFF" stroke-width="4" opacity=".85"/>' for _ in range(40))
b+=f'<path d="M-20,1260 Q260,1200 540,1250 T{W+20},1230 L{W+20},{H} L-20,{H} Z" fill="#2E6FA8" opacity=".7"/>'
b+=f'<path d="M-20,1450 Q300,1390 600,1440 T{W+20},1420 L{W+20},{H+20} L-20,{H+20} Z" fill="url(#sand)" {st(7)}/>'
b+=''.join(f'<circle cx="{r.uniform(0,W):.0f}" cy="{r.uniform(1500,1910):.0f}" r="5" fill="#B48A44" opacity=".5"/>' for _ in range(90))
def seaweed(x,y,h,c='#3FBF5A'):
    pts=' '.join(f'{x+math.sin(i*.9)*28:.0f},{y-i*h/8:.0f}' for i in range(9))
    return f'<polyline points="{pts}" fill="none" stroke="{O}" stroke-width="34" stroke-linecap="round" stroke-linejoin="round"/><polyline points="{pts}" fill="none" stroke="{c}" stroke-width="22" stroke-linecap="round" stroke-linejoin="round"/>'
b+=seaweed(80,1880,820)+seaweed(160,1890,560,'#2FA84C')+seaweed(1000,1870,740)+seaweed(915,1885,480,'#2FA84C')
def coral(x,y,s,c):
    return f'<g transform="translate({x},{y}) scale({s})" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M0,0 L0,-120 M0,-70 L-60,-140 M-60,-140 L-70,-200 M-60,-140 L-110,-170 M0,-120 L50,-190 M50,-190 L40,-240 M50,-190 L100,-220 M0,-60 L70,-110" stroke="{O}" stroke-width="46"/><path d="M0,0 L0,-120 M0,-70 L-60,-140 M-60,-140 L-70,-200 M-60,-140 L-110,-170 M0,-120 L50,-190 M50,-190 L40,-240 M50,-190 L100,-220 M0,-60 L70,-110" stroke="{c}" stroke-width="32"/></g>'
b+=coral(330,1890,1.15,'#FF6F91')+coral(790,1880,1.2,'#FF9F43')+coral(650,1905,.7,'#C77DFF')
b+=f'<path d="M420,1860 Q410,1780 500,1770 Q580,1740 640,1790 Q710,1800 700,1870 Z" fill="#8A84A8" {st(7)}/>'
b+=f'<path transform="translate(560,1890) rotate(10)" d="M0,-40 L12,-12 L40,-10 L18,8 L25,38 L0,20 L-25,38 L-18,8 L-40,-10 L-12,-12 Z" fill="#FFD43B" {st(6)}/>'
def fish(x,y,s,c,flip=1):
    return f'<g transform="translate({x},{y}) scale({s*flip},{s})"><path d="M-70,0 Q-30,-46 30,-30 Q70,-18 80,0 Q70,18 30,30 Q-30,46 -70,0 Z" fill="{c}" {st(6)}/><path d="M-66,0 L-120,-38 L-108,0 L-120,38 Z" fill="{c}" {st(6)}/><circle cx="44" cy="-6" r="10" fill="#FFFFFF" {st(4)}/><circle cx="47" cy="-6" r="4" fill="{O}"/><path d="M-10,-34 Q0,0 -10,34" fill="none" stroke="#FFFFFF" stroke-width="8" opacity=".8"/></g>'
b+=fish(780,420,1,'#FFB703',-1)+fish(880,520,.65,'#FF6F91',-1)+fish(260,300,.8,'#8DE08A')+fish(330,820,.55,'#C77DFF')+fish(760,1050,.7,'#5FD0FF',-1)
S['ocean']=svg(d,b)

# ---------------------------------------------------------------- 5. ESPACE
d=lg('sp',[(0,'#0D0828'),(1,'#2A1760')])+lg('gr',[(0,'#C9C2E6'),(1,'#9A90C4')])+lg('pl',[(0,'#FFB36B'),(1,'#E8574A')],0,0,1,1)+lg('pl2',[(0,'#7FE3FF'),(1,'#3B7BFF')],0,0,1,1)
b=f'<rect width="{W}" height="{H}" fill="url(#sp)"/>'
b+=f'<g filter="url(#blur40)" opacity=".55"><ellipse cx="300" cy="420" rx="360" ry="200" fill="#B154D8"/><ellipse cx="800" cy="900" rx="340" ry="180" fill="#3A6BFF"/><ellipse cx="400" cy="1150" rx="300" ry="130" fill="#FF6FB1"/></g>'
b+=stars(230,21,0,0,W,1400)
b+=f'<g transform="translate(700,560) scale(.95)"><ellipse rx="300" ry="60" fill="none" stroke="#FFE7B0" stroke-width="26" transform="rotate(-14)"/><circle r="170" fill="url(#pl)" {st(8)}/><path d="M-160,-40 Q0,-10 165,-60 M-150,60 Q0,90 150,40" fill="none" stroke="#C9452F" stroke-width="22" opacity=".55"/><path d="M-300,72 A300,60 0 0 0 290,-80" transform="rotate(-14)" fill="none" stroke="#FFE7B0" stroke-width="26"/></g>'
b+=f'<circle cx="230" cy="230" r="80" fill="url(#pl2)" {st(7)}/><path d="M180,200 q30,-20 60,0 q20,20 50,10 M170,260 q40,10 80,-10" fill="none" stroke="#FFFFFF" stroke-width="10" stroke-linecap="round" opacity=".6"/>'
b+=f'<g transform="translate(420,960) rotate(-30)"><path d="M0,0 L-160,0" stroke="#FFFFFF" stroke-width="6" opacity=".6" stroke-linecap="round"/><circle r="10" fill="#FFF6C9"/></g>'
b+=f'<path d="M-20,1400 Q240,1340 540,1380 T{W+20},1370 L{W+20},{H+20} L-20,{H+20} Z" fill="url(#gr)" {st(7)}/>'
for cx,cy,rx in [(180,1560,100),(560,1660,70),(300,1820,120),(760,1500,50),(520,1880,60)]:
    b+=f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{rx*.32}" fill="#8A80B6" {st(6)}/><ellipse cx="{cx}" cy="{cy+rx*.06}" rx="{rx*.75}" ry="{rx*.2}" fill="#7A70A8"/>'
b+=f'''<g transform="translate(900,1720) rotate(8) scale(.9)"><path d="M0,-330 Q70,-250 70,-110 L70,20 L-70,20 L-70,-110 Q-70,-250 0,-330 Z" fill="#FFFFFF" {st(8)}/>
<path d="M0,-330 Q45,-290 60,-240 L-60,-240 Q-45,-290 0,-330 Z" fill="#FF4D4D" {st(6)}/><circle cy="-150" r="36" fill="#7FE3FF" {st(7)}/><circle cx="-10" cy="-160" r="10" fill="#FFFFFF"/>
<path d="M-70,-40 L-130,40 L-70,20 Z M70,-40 L130,40 L70,20 Z" fill="#FF4D4D" {st(7)}/><path d="M-40,20 L40,20 L26,60 L-26,60 Z" fill="#8A80B6" {st(6)}/></g>'''
S['espace']=svg(d,b)

# ---------------------------------------------------------------- 6. JUNGLE
d=lg('sky',[(0,'#9FE7C9'),(1,'#E9FFF2')])+lg('wf',[(0,'#BFF4FF'),(1,'#5FD0F0')],0,0,1,0)+lg('ground',[(0,'#7BC24A'),(1,'#4E9A34')])
b=f'<rect width="{W}" height="{H}" fill="url(#sky)"/>'
b+=hill(1000,70,'#7FD19A',4)+hill(1130,60,'#4FB878',9)
b+=f'<path d="M420,620 Q540,590 660,620 L700,1380 L380,1380 Z" fill="#6E6A8E" {st(7)}/><path d="M455,628 Q540,612 625,628 L655,1380 L425,1380 Z" fill="url(#wf)" {st(6)}/>'
b+=''.join(f'<path d="M{x},{y} l0,110" stroke="#FFFFFF" stroke-width="8" stroke-linecap="round" opacity=".85"/>' for x,y in [(490,700),(540,880),(590,760),(500,1080),(580,1160)])
b+=f'<ellipse cx="540" cy="1390" rx="230" ry="46" fill="#BFF4FF" {st(6)}/>'
b+=f'<path d="M-20,1390 Q300,1340 540,1390 T{W+20},1380 L{W+20},{H+20} L-20,{H+20} Z" fill="url(#ground)" {st(7)}/><path d="M300,{H} C400,1760 600,1720 540,1520 C510,1450 520,1410 530,1400 L570,1400 C590,1420 610,1450 620,1520 C700,1740 620,1800 800,{H} Z" fill="#D9B46A" {st(6)}/>'
def leaf(x,y,ang,s,c='#2FA84C'):
    return f'<g transform="translate({x},{y}) rotate({ang}) scale({s})"><path d="M0,0 Q120,-90 300,-10 Q140,80 0,0 Z" fill="{c}" {st(7)}/><path d="M10,0 Q150,-20 290,-10" fill="none" stroke="#1E7E3A" stroke-width="6"/>'+''.join(f'<path d="M{60+i*45},{-5-i} l30,-40 M{60+i*45},{-5-i} l30,36" stroke="#1E7E3A" stroke-width="5" fill="none"/>' for i in range(5))+'</g>'
for x,y,a,s,c in [(-40,260,20,1.3,'#2FA84C'),(-60,620,-10,1.4,'#3FBF5A'),(-40,980,-25,1.3,'#2FA84C'),(-30,1360,-30,1.2,'#3FBF5A'),(W+40,340,160,1.4,'#3FBF5A'),(W+40,720,195,1.5,'#2FA84C'),(W+30,1100,210,1.2,'#3FBF5A'),(260,-40,70,1.1,'#3FBF5A'),(820,-40,110,1.2,'#2FA84C')]:
    b+=leaf(x,y,a,s,c)
b+=''.join(f'<g transform="translate({x},{y}) scale({s})"><circle cx="-70" cy="-40" r="70" fill="#3E9E4E" {st(7)}/><circle cx="40" cy="-70" r="85" fill="#4FB45E" {st(7)}/><circle cx="130" cy="-30" r="60" fill="#3E9E4E" {st(7)}/><rect x="-140" y="-30" width="330" height="40" fill="#3E9E4E"/><circle cx="20" cy="-100" r="22" fill="#7FE08A"/></g>' for x,y,s in [(150,1440,.9),(880,1430,.9)])
b+=''.join(f'<path d="M{x},-10 Q{x+30},{h*.5} {x},{h}" fill="none" stroke="{O}" stroke-width="16" stroke-linecap="round"/><path d="M{x},-10 Q{x+30},{h*.5} {x},{h}" fill="none" stroke="#6BAE3A" stroke-width="8" stroke-linecap="round"/>' for x,h in [(330,620),(760,520),(880,760)])
for x,y,c in [(160,1700,'#FF6F91'),(900,1640,'#FFB703'),(960,1820,'#FF6F91'),(120,1860,'#C77DFF')]:
    b+=f'<g transform="translate({x},{y})">'+''.join(f'<ellipse cx="{math.cos(math.radians(a))*22:.0f}" cy="{math.sin(math.radians(a))*22:.0f}" rx="20" ry="14" transform="rotate({a} {math.cos(math.radians(a))*22:.0f} {math.sin(math.radians(a))*22:.0f})" fill="{c}" {st(5)}/>' for a in range(0,360,72))+f'<circle r="12" fill="#FFE36B" {st(5)}/></g>'
S['jungle']=svg(d,b)

# ---------------------------------------------------------------- 7. CHÂTEAU
d=lg('sky',[(0,'#6CC8FF'),(1,'#D9F3FF')])+lg('stone',[(0,'#D7D2EA'),(1,'#B3ACD2')])
b=f'<rect width="{W}" height="{H}" fill="url(#sky)"/>'+cloud(260,230,.9)+cloud(820,160,1)+cloud(700,430,.5)
b+=hill(1180,40,'#9EDB8A',2)
def tower(x,y,w,h,roof='#FF5A5A'):
    t=f'<rect x="{x-w/2}" y="{y-h}" width="{w}" height="{h}" fill="url(#stone)" {st(7)}/>'
    t+=f'<path d="M{x-w/2-14},{y-h} L{x},{y-h-w*1.1} L{x+w/2+14},{y-h} Z" fill="{roof}" {st(7)}/>'
    t+=f'<path d="M{x},{y-h-w*1.1} L{x},{y-h-w*1.1-70}" {st(6)}/><path d="M{x},{y-h-w*1.1-70} L{x+60},{y-h-w*1.1-55} L{x},{y-h-w*1.1-38} Z" fill="#FFD43B" {st(5)}/>'
    t+=f'<path d="M{x-12},{y-h+60} q12,-20 24,0 L{x+12},{y-h+110} L{x-12},{y-h+110} Z" fill="{O}"/>'
    return t
c=tower(600,760,150,520)+tower(1320,760,150,520)
c+=f'<rect x="660" y="430" width="600" height="330" fill="url(#stone)" {st(7)}/>'
c+=''.join(f'<rect x="{x}" y="398" width="46" height="40" fill="url(#stone)" {st(6)}/>' for x in range(668,1250,90))
c+=tower(960,560,190,380,'#3BA7FF')
c+=f'<path d="M880,760 L880,640 Q960,560 1040,640 L1040,760 Z" fill="#8A5229" {st(7)}/>'+''.join(f'<path d="M{x},640 L{x},760" stroke="#5E3A1C" stroke-width="5"/>' for x in [920,960,1000])
c+=''.join(f'<path d="M{x},520 l0,30" stroke="{O}" stroke-width="14" stroke-linecap="round"/>' for x in [740,810,1110,1180])
b+=f'<g transform="translate(-420,610)">{c}</g>'
b+=f'<path d="M-20,1370 Q300,1330 540,1370 T{W+20},1360 L{W+20},{H+20} L-20,{H+20} Z" fill="#6FCB5A" {st(7)}/>'
b+=f'<path d="M300,{H} Q480,1600 480,1370 L600,1370 Q600,1600 780,{H} Z" fill="#E8D3A2" {st(6)}/>'
def tree(x,y,s=1):
    return f'<g transform="translate({x},{y}) scale({s})"><rect x="-18" y="-120" width="36" height="120" fill="#8A5229" {st(6)}/><circle cx="0" cy="-190" r="100" fill="#3FBF5A" {st(7)}/><circle cx="-70" cy="-140" r="60" fill="#3FBF5A" {st(7)}/><circle cx="70" cy="-140" r="60" fill="#3FBF5A" {st(7)}/><circle cx="-30" cy="-210" r="26" fill="#7FE08A"/><circle cx="-60" cy="-120" r="10" fill="#FF5A5A" {st(3)}/><circle cx="40" cy="-160" r="10" fill="#FF5A5A" {st(3)}/></g>'
b+=tree(110,1820,1.2)+tree(990,1790,1.1)
for x,y,c in [(250,1600,'#FF6F91'),(330,1680,'#FFD43B'),(820,1620,'#FFFFFF'),(880,1700,'#FF6F91')]:
    b+=f'<circle cx="{x}" cy="{y}" r="14" fill="{c}" {st(4)}/><circle cx="{x}" cy="{y}" r="5" fill="#FFB703"/>'
S['chateau']=svg(d,b)

# ---------------------------------------------------------------- 8. VOLCAN
d=lg('sky',[(0,'#3A1E4F'),(.5,'#C2453B'),(1,'#FF9A4A')])+lg('lava',[(0,'#FFE36B'),(1,'#FF5A1F')])+lg('rock',[(0,'#4A3B57'),(1,'#2D2338')])
b=f'<rect width="{W}" height="{H}" fill="url(#sky)"/>'
b+=f'<g filter="url(#blur12)" opacity=".75">'+''.join(f'<circle cx="{540+dx}" cy="{330+dy}" r="{rr}" fill="#5E4A68"/>' for dx,dy,rr in [(-120,0,120),(0,-80,150),(140,-20,130),(260,-120,110),(-260,-110,100),(60,-220,120)])+'</g>'
b+=f'<path d="M20,1400 L430,640 Q540,610 650,640 L1060,1400 Z" fill="#6A4E6E" {st(8)}/><path d="M430,640 Q540,672 650,640 Q590,620 540,620 Q490,620 430,640 Z" fill="#FF5A1F" {st(6)}/>'
b+=f'<path d="M505,640 Q480,800 540,940 Q600,1080 520,1400 L620,1400 Q670,1100 610,940 Q570,800 580,640 Z" fill="url(#lava)" {st(6)}/>'
b+=f'<g filter="url(#glow)">'+''.join(f'<circle cx="{540+dx}" cy="{560+dy}" r="{rr}" fill="{c}" {st(5)}/>' for dx,dy,rr,c in [(0,-40,34,'#FFE36B'),(-90,-110,24,'#FF9A3C'),(100,-140,28,'#FFE36B'),(-30,-230,20,'#FF9A3C'),(40,-70,16,'#FFFFFF'),(150,-280,18,'#FFE36B')])+'</g>'
b+=f'<path d="M-20,1400 Q260,1360 540,1400 T{W+20},1390 L{W+20},{H+20} L-20,{H+20} Z" fill="url(#rock)" {st(7)}/>'
b+=f'<path d="M-20,1580 Q200,1530 400,1570 Q560,1600 700,1560 L710,1590 Q560,1630 400,1602 Q200,1565 -20,1615 Z" fill="url(#lava)" {st(6)}/>'
b+=f'<path d="M700,{H} Q760,1800 880,1780 Q980,1760 {W+20},1770 L{W+20},{H} Z" fill="url(#lava)" {st(6)}/>'
for x,y,s in [(170,1480,1),(900,1470,1.1),(380,1860,.9),(760,1520,.6)]:
    b+=f'<path transform="translate({x},{y}) scale({s})" d="M-90,30 Q-100,-40 -30,-60 Q30,-90 80,-40 Q120,0 90,30 Z" fill="#5A4868" {st(7)}/>'
def fern(x,y,s=1):
    return f'<g transform="translate({x},{y}) scale({s})">'+''.join(f'<path d="M0,0 Q{dx*.5},{-120} {dx},{-200+abs(dx)*.4}" fill="none" stroke="{O}" stroke-width="22" stroke-linecap="round"/><path d="M0,0 Q{dx*.5},{-120} {dx},{-200+abs(dx)*.4}" fill="none" stroke="#3E8E4A" stroke-width="12" stroke-linecap="round"/>' for dx in [-160,-80,0,80,160])+'</g>'
b+=fern(70,1910,1.2)+fern(1010,1910,1.1)
S['volcan']=svg(d,b)

# ---------------------------------------------------------------- 9. FAR WEST
d=lg('sky',[(0,'#FF9E5E'),(.6,'#FFD08A'),(1,'#FFE9B8')])+lg('sand',[(0,'#F2B266'),(1,'#D98C42')])+lg('mesa',[(0,'#D8643A'),(1,'#B2462B')])
b=f'<rect width="{W}" height="{H}" fill="url(#sky)"/><circle cx="540" cy="1000" r="300" fill="#FFF3A6" opacity=".25"/><circle cx="540" cy="1000" r="220" fill="#FFE36B" {st(8)}/>'
b+=''.join(f'<path d="M{x},{y} q50,-26 110,-6 q50,-20 100,4" fill="none" stroke="#FFF3D6" stroke-width="16" stroke-linecap="round" opacity=".8"/>' for x,y in [(120,330),(640,220),(360,560)])
b+=''.join(f'<path d="M{x},{y} q18,-16 36,0 q18,-16 36,0" fill="none" {st(6)}/>' for x,y in [(760,480),(830,430)])
b+=f'<path d="M-20,1140 L60,1140 L100,900 L400,900 L440,1140 L700,1140 L740,960 L1000,960 L1040,1140 L{W+20},1140 L{W+20},1320 L-20,1320 Z" fill="url(#mesa)" {st(7)}/>'
b+=''.join(f'<path d="M{x0},{y} L{x1},{y}" stroke="#9E3A22" stroke-width="6" opacity=".6"/>' for x0,x1,y in [(110,390,970),(90,410,1050),(750,990,1020),(735,1000,1080)])
b+=f'<path d="M-20,1300 Q300,1260 540,1300 T{W+20},1290 L{W+20},{H+20} L-20,{H+20} Z" fill="url(#sand)" {st(7)}/>'
def cactus(x,y,s=1):
    g='#3FA35A'
    return f'''<g transform="translate({x},{y}) scale({s})"><path d="M-40,0 L-40,-380 Q-40,-430 0,-430 Q40,-430 40,-380 L40,0 Z" fill="{g}" {st(7)}/>
<path d="M-40,-200 L-110,-200 Q-140,-200 -140,-240 L-140,-320 Q-140,-350 -112,-350 Q-86,-350 -86,-320 L-86,-250 L-40,-250 Z" fill="{g}" {st(7)}/>
<path d="M40,-150 L110,-150 Q140,-150 140,-190 L140,-290 Q140,-320 112,-320 Q86,-320 86,-290 L86,-200 L40,-200 Z" fill="{g}" {st(7)}/>
<path d="M0,-410 L0,-20 M-112,-335 L-112,-215 M112,-305 L112,-165" stroke="#2C8A47" stroke-width="6" fill="none"/><circle cx="0" cy="-440" r="14" fill="#FF6F91" {st(4)}/></g>'''
b+=cactus(160,1840,1.35)+cactus(560,1340,.35)
b+=f'<g transform="translate(800,1820) scale(.8)"><rect x="-200" y="-330" width="400" height="330" fill="#B87437" {st(7)}/><path d="M-230,-330 L230,-330 L230,-420 L140,-420 L140,-450 L-140,-450 L-140,-420 L-230,-420 Z" fill="#C98A4B" {st(7)}/>'+''.join(f'<path d="M-200,{-310+i*40} L200,{-310+i*40}" stroke="#8A5229" stroke-width="4"/>' for i in range(8))+'<rect x="-60" y="-190" width="120" height="190" fill="#5E3A1C" stroke="#2B2245" stroke-width="7"/><path d="M-60,-150 L-2,-150 L-2,-50 L-60,-50 Z M2,-150 L60,-150 L60,-50 L2,-50 Z" fill="#C98A4B" stroke="#2B2245" stroke-width="6"/><rect x="-170" y="-260" width="80" height="70" fill="#FFE36B" stroke="#2B2245" stroke-width="6"/><rect x="90" y="-260" width="80" height="70" fill="#FFE36B" stroke="#2B2245" stroke-width="6"/><rect x="-110" y="-410" width="220" height="56" rx="8" fill="#FFF3D6" stroke="#2B2245" stroke-width="6"/><path d="M-80,-382 L80,-382" stroke="#B2462B" stroke-width="10" stroke-linecap="round"/></g>'
b+=f'<g transform="translate(470,1860)"><circle r="56" fill="none" stroke="#B88A4A" stroke-width="10"/><path d="M-40,-30 Q0,10 40,-30 M-50,10 Q0,-30 50,20 M-20,-50 Q10,0 -10,50 M20,-50 Q-10,0 30,46" fill="none" stroke="#B88A4A" stroke-width="8"/></g>'
S['farwest']=svg(d,b)

# ---------------------------------------------------------------- 10. MONTAGNE
d=lg('sky',[(0,'#7CC7FF'),(1,'#E4F4FF')])+lg('mt',[(0,'#9FB0E0'),(1,'#7A8CC4')])+lg('snow',[(0,'#FFFFFF'),(1,'#DCEBFF')])
b=f'<rect width="{W}" height="{H}" fill="url(#sky)"/>'+cloud(820,220,.8)+cloud(250,330,.6)
for x,h,c in [(180,760,'#8FA2D8'),(620,940,'#7A8CC4'),(1020,700,'#8FA2D8')]:
    b+=f'<path d="M{x-460},1360 L{x},{1360-h} L{x+460},1360 Z" fill="{c}" {st(8)}/><path d="M{x-150},{1360-h+200} L{x},{1360-h} L{x+150},{1360-h+200} q-30,30 -60,0 q-30,30 -60,0 q-30,30 -60,0 q-30,30 -30,0 z" fill="#FFFFFF" {st(6)}/>'
b+=f'<path d="M-20,1340 Q300,1290 540,1340 T{W+20},1330 L{W+20},{H+20} L-20,{H+20} Z" fill="url(#snow)" {st(7)}/>'
b+=''.join(pine(x,y,h,'#2E8B57',True) for x,y,h in [(90,1800,460),(250,1560,280),(1000,1830,440),(880,1500,240)])
b+=f'''<g transform="translate(620,1780) scale(.85)"><rect x="-170" y="-200" width="340" height="200" fill="#B87437" {st(7)}/>{''.join(f'<path d="M-170,{-180+i*36} L170,{-180+i*36}" stroke="#8A5229" stroke-width="5"/>' for i in range(5))}
<path d="M-220,-190 L0,-360 L220,-190 Z" fill="#8A5229" {st(7)}/><path d="M-235,-185 L0,-372 L235,-185 q-40,24 -80,0 q-40,24 -80,0 q-40,24 -80,0 q-40,24 -80,0 q-40,24 -80,0 q-30,20 -70,0 z" fill="#FFFFFF" {st(6)}/>
<rect x="-120" y="-140" width="80" height="70" fill="#FFD45E" {st(6)}/><path d="M-80,-140 L-80,-70 M-120,-105 L-40,-105" {st(5)}/><rect x="40" y="-120" width="80" height="120" fill="#5E3A1C" {st(6)}/><circle cx="104" cy="-60" r="6" fill="#FFD43B"/>
<rect x="90" y="-330" width="50" height="90" fill="#8A84A8" {st(6)}/></g>'''
b+=f'<g transform="translate(330,1860)"><circle cy="-60" r="70" fill="#FFFFFF" {st(7)}/><circle cy="-170" r="50" fill="#FFFFFF" {st(7)}/><circle cx="-16" cy="-180" r="7" fill="{O}"/><circle cx="16" cy="-180" r="7" fill="{O}"/><path d="M0,-166 L44,-158 L0,-150 Z" fill="#FF9F43" {st(4)}/><path d="M-50,-128 Q0,-110 50,-128 L46,-112 Q0,-96 -46,-112 Z" fill="#FF4D4D" {st(5)}/><circle cy="-70" r="7" fill="{O}"/><circle cy="-40" r="7" fill="{O}"/></g>'
r=random.Random(31)
b+=''.join(f'<circle cx="{r.uniform(0,W):.0f}" cy="{r.uniform(0,1320):.0f}" r="{r.choice([4,5,7])}" fill="#FFFFFF" opacity=".85"/>' for _ in range(80))
S['montagne']=svg(d,b)

# ---------------------------------------------------------------- 11. THÉÂTRE
d=lg('back',[(0,'#2A1758'),(1,'#4A2A84')])+lg('cur',[(0,'#E33A3A'),(.5,'#B8202A'),(1,'#E33A3A')],0,0,1,0)+lg('floor',[(0,'#C98A4B'),(1,'#8A5229')])
FL=1420
b=f'<rect width="{W}" height="{H}" fill="url(#back)"/>'+stars(60,44,200,320,880,1300,'#FFE9A6')
b+=''.join(f'<path d="M{x},230 L{x-240},{FL} L{x+240},{FL} Z" fill="#FFF3B0" opacity=".14"/>' for x in [380,700])
b+=f'<path d="M-20,{FL} L{W+20},{FL} L{W+20},{H+20} L-20,{H+20} Z" fill="url(#floor)" {st(7)}/>'
b+=''.join(f'<path d="M{W/2+i*70},{FL} L{W/2+i*160},{H}" stroke="#7E4A22" stroke-width="4"/>' for i in range(-9,10))
b+=''.join(f'<ellipse cx="{x}" cy="{FL}" rx="220" ry="40" fill="#FFF3B0" opacity=".25"/>' for x in [380,700])
b+=f'<rect x="-20" y="{FL-10}" width="{W+40}" height="24" fill="#5E3A1C" {st(6)}/>'
def curtain(x0,x1,side,bottom):
    folds=5;w=(x1-x0)/folds;out=''
    for i in range(folds):
        a=x0+i*w;out+=f'<path d="M{a},-20 L{a+w},-20 L{a+w+(side*10)},{bottom} Q{a+w/2},{bottom+40} {a+(side*10)},{bottom} Z" fill="url(#cur)" {st(6)}/>'
    return out
b+=curtain(-60,220,1,FL+20)+curtain(860,1140,-1,FL+20)
b+=f'<path d="M110,800 Q220,830 260,800" fill="none" stroke="#FFD43B" stroke-width="22" stroke-linecap="round"/><circle cx="260" cy="806" r="22" fill="#FFD43B" {st(5)}/><path d="M970,800 Q860,830 820,800" fill="none" stroke="#FFD43B" stroke-width="22" stroke-linecap="round"/><circle cx="820" cy="806" r="22" fill="#FFD43B" {st(5)}/>'
b+=f'<path d="M-20,-20 L{W+20},-20 L{W+20},200 '+''.join(f'Q{W-i*216-108},{280} {W-(i+1)*216},200 ' for i in range(5))+f'L-20,200 Z" fill="url(#cur)" {st(7)}/>'
b+=f'<path d="M-20,190 '+''.join(f'Q{i*216+108},{270} {(i+1)*216},190 ' for i in range(5))+'" fill="none" stroke="#FFD43B" stroke-width="16"/>'
b+=''.join(f'<g transform="translate({x},255)"><path d="M0,-30 L0,0" {st(5)}/><path d="M-14,0 L14,0 L20,50 L-20,50 Z" fill="#FFD43B" {st(5)}/></g>' for x in range(108,W,216))
b+=''.join(f'<path d="M{x-30},{H+10} L{x-20},{H-40} L{x+20},{H-40} L{x+30},{H+10} Z" fill="#3B3560" {st(5)}/><ellipse cx="{x}" cy="{H-44}" rx="18" ry="8" fill="#FFE36B"/>' for x in range(140,W,270))
S['theatre']=svg(d,b)

# ---------------------------------------------------------------- 12. MANOIR HANTÉ
d=lg('sky',[(0,'#1A1240'),(.65,'#3D2470'),(1,'#5E3A8C')])+rg('mg',[(0,'#E8FFC9',.5),(1,'#E8FFC9',0)])+lg('hill',[(0,'#3A2E5E'),(1,'#241C40')])
b=f'<rect width="{W}" height="{H}" fill="url(#sky)"/>'+stars(120,77,0,0,W,1000)
b+=f'<circle cx="760" cy="330" r="300" fill="url(#mg)"/><circle cx="760" cy="330" r="160" fill="#F4FFD6" {st(8)}/>'+''.join(f'<circle cx="{760+dx}" cy="{330+dy}" r="{rr}" fill="#DCEBB8" {st(4)}/>' for dx,dy,rr in [(-50,-40,26),(40,30,34),(-10,70,16)])
b+=''.join(f'<path transform="translate({x},{y}) scale({s})" d="M0,0 Q-20,-24 -46,-10 Q-60,-24 -80,-8 Q-56,-4 -50,16 Q-30,6 0,12 Q30,6 50,16 Q56,-4 80,-8 Q60,-24 46,-10 Q20,-24 0,0 Z" fill="{O}"/>' for x,y,s in [(560,250,1),(900,560,.7),(380,480,.55),(200,700,.6)])
b+=f'<path d="M-20,1180 Q300,1060 600,1120 T{W+20},1100 L{W+20},{H+20} L-20,{H+20} Z" fill="url(#hill)" {st(7)}/>'
b+=f'''<g transform="translate(540,1300) scale(.95)"><rect x="-260" y="-260" width="520" height="260" fill="#5B4A86" {st(7)}/><path d="M-300,-250 L0,-420 L300,-250 Z" fill="#3B2E64" {st(7)}/>
<rect x="160" y="-470" width="110" height="250" fill="#5B4A86" {st(7)}/><path d="M140,-470 L215,-570 L290,-470 Z" fill="#3B2E64" {st(7)}/>
<rect x="-60" y="-140" width="120" height="140" rx="60" fill="#2B2245" {st(6)}/>
{''.join(f'<rect x="{x}" y="{y}" width="70" height="80" rx="6" fill="#FFD45E" {st(6)}/><path d="M{x+35},{y} L{x+35},{y+80} M{x},{y+40} L{x+70},{y+40}" {st(4)}/>' for x,y in [(-220,-210),(-120,-210),(50,-210),(150,-210),(-220,-110),(150,-110),(180,-420)])}
<circle cx="0" cy="-320" r="34" fill="#FFD45E" {st(6)}/></g>'''
def bare_tree(x,y,s=1):
    return f'<g transform="translate({x},{y}) scale({s})" fill="none" stroke-linecap="round"><path d="M0,0 L0,-260 M0,-180 L-90,-260 M-90,-260 L-120,-320 M-90,-260 L-150,-270 M0,-260 L70,-340 M70,-340 L60,-400 M70,-340 L130,-360 M0,-120 L80,-170" stroke="{O}" stroke-width="40"/><path d="M0,0 L0,-260 M0,-180 L-90,-260 M-90,-260 L-120,-320 M-90,-260 L-150,-270 M0,-260 L70,-340 M70,-340 L60,-400 M70,-340 L130,-360 M0,-120 L80,-170" stroke="#4A3A6A" stroke-width="26"/></g>'
b+=bare_tree(120,1780,1.5)+bare_tree(960,1760,1.25)
FY=1480
b+=''.join(f'<path d="M{x},{FY+40} L{x},{FY-30}" stroke="{O}" stroke-width="14" stroke-linecap="round"/><path d="M{x-8},{FY-25} L{x},{FY-45} L{x+8},{FY-25}" fill="{O}"/>' for x in range(20,W,70) if not 430<x<650)
b+=f'<path d="M-20,{FY-10} L{W+20},{FY-10}" stroke="{O}" stroke-width="12"/>'
b+=f'<path d="M-20,1520 Q300,1480 600,1520 T{W+20},1510 L{W+20},{H+20} L-20,{H+20} Z" fill="#2B2350" {st(7)}/>'
for x,y,s in [(330,1650,.9),(760,1640,.8),(860,1880,1)]:
    b+=f'<path transform="translate({x},{y}) scale({s})" d="M-50,0 L-50,-100 Q-50,-150 0,-150 Q50,-150 50,-100 L50,0 Z" fill="#8A84A8" {st(7)}/><path transform="translate({x},{y}) scale({s})" d="M-24,-90 L24,-90 M0,-112 L0,-60" stroke="#5E5A73" stroke-width="10" stroke-linecap="round"/>'
def pumpkin(x,y,s=1):
    return f'<g transform="translate({x},{y}) scale({s})"><ellipse rx="80" ry="62" fill="#FF8A2B" {st(7)}/><ellipse rx="34" ry="62" fill="none" {st(5)}/><path d="M0,-60 Q4,-90 24,-96" fill="none" stroke="#3E8E4A" stroke-width="14" stroke-linecap="round"/><path d="M-44,-14 L-24,-30 L-14,-8 Z M44,-14 L24,-30 L14,-8 Z" fill="#FFE36B" {st(4)}/><path d="M-40,20 Q0,46 40,20 Q20,30 0,26 Q-20,30 -40,20 Z" fill="#FFE36B" {st(4)}/></g>'
b+=pumpkin(560,1850)+pumpkin(680,1880,.6)+pumpkin(250,1890,.7)
S['manoir']=svg(d,b)

if __name__=='__main__':
    out=sys.argv[1]
    for k,v in S.items(): open(os.path.join(out,k+'.svg'),'w').write(v)
    print(len(S),'scènes verticales')
