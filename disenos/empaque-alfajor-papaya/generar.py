"""Genera la cara frontal del empaque (flow pack) del Alfajor Blanco de Papaya.

Unidades en milímetros. Cara imprimible 100 x 90 mm + aletas de sellado de 6 mm.
Ejecutar: python3 generar.py  ->  frente.svg + index.html
"""
import math, random

W, H, FIN = 112, 90, 6          # ancho total, alto, aleta de sellado
X0, X1 = FIN, W - FIN           # cara imprimible: x 6..106
ORANGE = "#E2832A"
ORANGE_DK = "#B85F17"
CREAM = "#FFF3DC"
BROWN = "#6E3410"
SEAL = 25                       # sello 2,5 x 2,5 cm (cara 90 cm2, rango 60-100 cm2)

random.seed(7)
el = []

def star(cx, cy, r, fill="url(#gold)", op=1):
    k = r * 0.28
    return (f'<path d="M{cx},{cy-r} Q{cx+k},{cy-k} {cx+r},{cy} Q{cx+k},{cy+k} {cx},{cy+r} '
            f'Q{cx-k},{cy+k} {cx-r},{cy} Q{cx-k},{cy-k} {cx},{cy-r}Z" fill="{fill}" opacity="{op}"/>')

# ---------- fondo ----------
el.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{ORANGE}"/>')
el.append(f'<rect x="{X0}" y="0" width="{X1-X0}" height="{H}" fill="url(#glow)"/>')

# constelaciones (patrón de fondo, "Región de las Estrellas")
g = ['<g stroke="#FCE3A6" stroke-width="0.18" opacity="0.24" fill="#FCE3A6">']
for _ in range(9):
    cx, cy = random.uniform(X0+4, X1-4), random.uniform(4, H-4)
    pts = [(cx + random.uniform(-9, 9), cy + random.uniform(-7, 7)) for _ in range(random.randint(3, 5))]
    pts.sort()
    g.append('<polyline fill="none" points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + '"/>')
    for x, y in pts:
        g.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{random.uniform(0.35,0.7):.2f}" stroke="none"/>')
for _ in range(60):
    g.append(f'<circle cx="{random.uniform(X0,X1):.1f}" cy="{random.uniform(0,H):.1f}" r="0.22" stroke="none"/>')
g.append('</g>')
el.append("".join(g))

# ---------- aletas de sellado (crimp) ----------
for fx in (0, X1):
    el.append(f'<rect x="{fx}" y="0" width="{FIN}" height="{H}" fill="{ORANGE_DK}"/>')
    for i in range(int(H / 1.6)):
        y = i * 1.6
        el.append(f'<line x1="{fx}" y1="{y}" x2="{fx+FIN}" y2="{y}" stroke="#8E4610" stroke-width="0.35"/>')

# ---------- logo (marcador: reemplazar por el vector original de Lili's) ----------
LX, LY, LR = 23, 17, 12.5
el.append(f'''
<g id="logo">
  <circle cx="{LX}" cy="{LY}" r="{LR}" fill="none" stroke="url(#gold)" stroke-width="0.9"/>
  <circle cx="{LX}" cy="{LY}" r="{LR-3.4}" fill="none" stroke="url(#gold)" stroke-width="0.4"/>
  <path id="arcTop" d="M{LX-LR+1.7},{LY} A{LR-1.7},{LR-1.7} 0 0 1 {LX+LR-1.7},{LY}" fill="none"/>
  <path id="arcBot" d="M{LX-LR+0.6},{LY} A{LR-0.6},{LR-0.6} 0 0 0 {LX+LR-0.6},{LY}" fill="none"/>
  <text font-family="Archivo" font-weight="700" font-size="2.3" letter-spacing="0.9" fill="url(#gold)">
    <textPath href="#arcTop" startOffset="50%" text-anchor="middle">DULCERÍA</textPath></text>
  <text font-family="Archivo" font-weight="700" font-size="2.1" letter-spacing="0.7" fill="url(#gold)">
    <textPath href="#arcBot" startOffset="50%" text-anchor="middle">ARTESANALES</textPath></text>
  <text x="{LX}" y="{LY+2.6}" text-anchor="middle" font-family="Great Vibes" font-size="9.6" fill="url(#gold)">Lili's</text>
  {star(LX, LY-6.2, 1.2)}
</g>''')

# ---------- peso neto ----------
el.append(f'<text x="{X1-3}" y="8.5" text-anchor="end" font-family="Archivo" font-weight="700" '
          f'font-size="2.9" letter-spacing="0.4" fill="{CREAM}">PESO NETO <tspan font-size="4.6">65 g</tspan></text>')

# ---------- papayas ----------
def papaya_whole(cx, cy, rot):
    return f'''<g transform="translate({cx},{cy}) rotate({rot})">
  <path d="M0,-11 C5.5,-10 7.2,-3 6.6,3 C6,8.5 3.4,11.5 0,11.5 C-3.4,11.5 -6,8.5 -6.6,3 C-7.2,-3 -5.5,-10 0,-11Z" fill="url(#skin)" stroke="{BROWN}" stroke-width="0.3"/>
  <path d="M0,-10.6 C2.2,-5 2.4,5 0,11.2 M-3.4,-9 C-4.6,-3 -4.4,5 -2.6,10.6 M3.4,-9 C4.6,-3 4.4,5 2.6,10.6" fill="none" stroke="#C9761F" stroke-width="0.35"/>
  <path d="M0,-11 L0,-12.6" stroke="{BROWN}" stroke-width="0.6" stroke-linecap="round"/>
</g>'''

def papaya_half(cx, cy, rot):
    seeds = "".join(
        f'<ellipse cx="{math.cos(a)*r:.2f}" cy="{math.sin(a)*r*1.5:.2f}" rx="0.55" ry="0.8" fill="#FFF6DA" stroke="#E0A54A" stroke-width="0.12"/>'
        for a, r in [(i*0.9, 1.2 + (i % 3)*0.7) for i in range(14)])
    return f'''<g transform="translate({cx},{cy}) rotate({rot})">
  <path d="M0,-11 C5.5,-10 7.2,-3 6.6,3 C6,8.5 3.4,11.5 0,11.5 C-3.4,11.5 -6,8.5 -6.6,3 C-7.2,-3 -5.5,-10 0,-11Z" fill="#F0B040" stroke="{BROWN}" stroke-width="0.3"/>
  <path d="M0,-9.8 C4.6,-9 6,-3 5.5,2.6 C5,7.4 2.8,10.2 0,10.2 C-2.8,10.2 -5,7.4 -5.5,2.6 C-6,-3 -4.6,-9 0,-9.8Z" fill="#FBDB8C"/>
  <path d="M0,-6.5 C2.8,-6 3.6,-1.5 3.3,2 C3,5 1.8,6.8 0,6.8 C-1.8,6.8 -3,5 -3.3,2 C-3.6,-1.5 -2.8,-6 0,-6.5Z" fill="#F4BE5C"/>
  <g transform="translate(0,0.4)">{seeds}</g>
</g>'''

el.append(papaya_whole(79, 26, -24))
el.append(papaya_half(94, 27, 14))
el.append(star(70.5, 15, 1.4, op=0.95) + star(68, 37, 1.1, op=0.9))

# ---------- faro monumental ----------
def faro(ox, oy, s=1):
    merl = lambda x0, x1, y, step=2.2, w=1.3, h=1.4: "".join(
        f'<rect x="{x:.2f}" y="{y-h}" width="{w}" height="{h}"/>' for x in [x0 + i*step for i in range(int((x1-x0)/step)+1)] if x + w <= x1 + 0.01)
    return f'''<g transform="translate({ox},{oy}) scale({s})" stroke="#C57F26" stroke-width="0.3" fill="{CREAM}" stroke-linejoin="round">
  <!-- ala derecha almenada -->
  <rect x="16.5" y="31" width="14.5" height="14"/>
  <g>{merl(16.5, 31, 31)}</g>
  <path d="M21.6,45 L21.6,40.4 A1.7,1.7 0 0 1 25,40.4 L25,45Z" fill="{BROWN}" stroke="none"/>
  <!-- ala izquierda -->
  <rect x="1" y="37" width="6.5" height="8"/>
  <g>{merl(1, 7.5, 37, 2.2, 1.2, 1.2)}</g>
  <!-- torre -->
  <path d="M7.2,45 L16.8,45 L16,12.5 L8,12.5Z"/>
  <line x1="7.6" y1="30" x2="16.4" y2="30"/><line x1="7.8" y1="21" x2="16.2" y2="21"/>
  <rect x="11.3" y="15.5" width="1.4" height="3" fill="{BROWN}" stroke="none"/>
  <rect x="11.3" y="24" width="1.4" height="3" fill="{BROWN}" stroke="none"/>
  <rect x="11.3" y="33" width="1.4" height="3" fill="{BROWN}" stroke="none"/>
  <!-- galería almenada -->
  <rect x="6.3" y="10" width="11.4" height="2.5"/>
  <g>{merl(6.3, 17.7, 10, 2.3, 1.4, 1.4)}</g>
  <!-- linterna y cúpula -->
  <rect x="9.3" y="4.2" width="5.4" height="4.4" fill="#FBE7B4"/>
  <line x1="12" y1="4.2" x2="12" y2="8.6"/>
  <path d="M9,4.2 Q12,0.3 15,4.2Z" fill="{BROWN}" stroke="none"/>
  <line x1="12" y1="1.4" x2="12" y2="-0.6" stroke="{BROWN}" stroke-width="0.4"/>
  <!-- haz de luz -->
  <path d="M14.7,5.6 L27,1.5 L27,9.2Z" fill="#FFF3C4" opacity="0.35" stroke="none"/>
  <!-- roca base -->
  <path d="M-1.5,47.5 Q4,44.2 10,45.2 Q17,44 24,45.2 Q30,44.4 34,47.5Z" fill="#8E4610" stroke="none"/>
</g>'''

el.append(faro(10, 38.5, 0.85))
el.append(star(38, 46, 1.4) + star(41.5, 52, 0.8, op=0.9) + star(35, 60, 0.7, op=0.8))
el.append(f'<text x="9.5" y="35.2" font-family="Great Vibes" font-size="4.4" fill="url(#gold)">La Región de las Estrellas</text>')

# ---------- título ----------
TX = 46
el.append(f'<text x="{TX}" y="45" font-family="Archivo" font-weight="700" font-size="2.35" letter-spacing="0.55" fill="#FCE3A6">RECUERDO DE COQUIMBO · CHILE</text>')
el.append(f'<text x="{TX}" y="51.6" font-family="Archivo Black" font-size="5.5" fill="{CREAM}">ALFAJOR BLANCO</text>')
el.append(f'<text x="{TX}" y="58.6" font-family="Archivo Black" font-size="6.8" fill="{CREAM}">DE PAPAYA</text>')
el.append(f'<text x="{X1-3}" y="40.2" text-anchor="end" font-family="Great Vibes" font-size="4.3" fill="url(#gold)">Alfajor Premium</text>')

# ---------- inglés + hecho a mano ----------
el.append(f'<text x="10" y="83.2" font-family="Archivo" font-weight="700" font-size="2.2" fill="{CREAM}">White chocolate papaya alfajor</text>')
el.append(f'<text x="10" y="86.6" font-family="Archivo" font-weight="500" font-size="2" fill="{CREAM}">Hecho a mano en Coquimbo, Chile</text>')

# ---------- sellos MINSAL (Ley 20.606) ----------
def sello(x, y, lines):
    s, c = SEAL, SEAL * 0.2929
    pts = f"{x+c},{y} {x+s-c},{y} {x+s},{y+c} {x+s},{y+s-c} {x+s-c},{y+s} {x+c},{y+s} {x},{y+s-c} {x},{y+c}"
    i = 1.1; ci = (s - 2*i) * 0.2929
    ip = f"{x+i+ci},{y+i} {x+s-i-ci},{y+i} {x+s-i},{y+i+ci} {x+s-i},{y+s-i-ci} {x+s-i-ci},{y+s-i} {x+i+ci},{y+s-i} {x+i},{y+s-i-ci} {x+i},{y+i+ci}"
    cx = x + s/2
    t = [f'<polygon points="{pts}" fill="#000"/>',
         f'<polygon points="{ip}" fill="none" stroke="#fff" stroke-width="0.45"/>',
         f'<text x="{cx}" y="{y+7.8}" text-anchor="middle" font-family="Arial, Liberation Sans, sans-serif" font-weight="700" font-size="3.4" fill="#fff">ALTO EN</text>']
    ys = [y+13.0] if len(lines) == 1 else [y+11.9, y+15.2]
    for ly, txt in zip(ys, lines):
        t.append(f'<text x="{cx}" y="{ly}" text-anchor="middle" font-family="Arial, Liberation Sans, sans-serif" font-weight="700" font-size="3.1" fill="#fff">{txt}</text>')
    t.append(f'<line x1="{x+5}" y1="{y+17.1}" x2="{x+s-5}" y2="{y+17.1}" stroke="#fff" stroke-width="0.3"/>')
    t.append(f'<text x="{cx}" y="{y+19.6}" text-anchor="middle" font-family="Arial, Liberation Sans, sans-serif" font-weight="700" font-size="1.6" fill="#fff">Ministerio de Salud</text>')
    return "".join(t)

SY = H - SEAL - 2.5
el.append(sello(X1 - 2 - 2*SEAL - 2, SY, ["AZÚCARES"]))
el.append(sello(X1 - 2 - SEAL, SY, ["GRASAS", "SATURADAS"]))

defs = f'''<defs>
  <linearGradient id="gold" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#FFF0C2"/><stop offset="0.45" stop-color="#F2C667"/>
    <stop offset="0.7" stop-color="#FBE3A0"/><stop offset="1" stop-color="#D9A441"/></linearGradient>
  <radialGradient id="glow" cx="0.55" cy="0.35" r="0.75">
    <stop offset="0" stop-color="#F0A043" stop-opacity="0.9"/><stop offset="1" stop-color="{ORANGE}" stop-opacity="0"/></radialGradient>
  <linearGradient id="skin" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#F7CB63"/><stop offset="1" stop-color="#E39A2F"/></linearGradient>
</defs>'''

svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}mm" height="{H}mm">'
       + defs + "\n".join(el) + '</svg>')
open("frente.svg", "w").write(svg)

fonts = open("fonts/local.css").read()
html = f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<title>Empaque Alfajor Blanco de Papaya</title>
<style>
{fonts}
body{{margin:0;background:#f1efec;display:grid;place-items:center;min-height:100vh}}
.frente{{width:1120px;filter:drop-shadow(0 18px 30px rgba(80,40,10,.25))}}
.frente svg{{width:100%;height:auto;display:block}}
</style></head>
<body><div class="frente">{svg}</div></body></html>'''
open("index.html", "w").write(html)
print("ok")
