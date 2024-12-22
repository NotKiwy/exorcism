import builtins
import sys
import os
import time
import shutil
from typing import List, Dict, Any

COLORS = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'cyan': (0, 255, 255),
    'magenta': (255, 0, 255),
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'orange': (255, 165, 0),
    'purple': (128, 0, 128),
    'pink': (255, 192, 203),
    'gray': (128, 128, 128)
}


def system(old_name, new_name):
    if hasattr(builtins, old_name):
        setattr(builtins, new_name, getattr(builtins, old_name))
        return True
    return False


def color(text, sc='white', ec='blue', d='h'):
    sr = COLORS.get(sc.lower(), COLORS['white'])
    er = COLORS.get(ec.lower(), COLORS['blue'])

    ls = text.split('\n')
    gt = []

    r1, g1, b1 = sr
    r2, g2, b2 = er

    if d == 'h':
        for l in ls:
            cl = ""
            for i, c in enumerate(l):
                rt = i / len(l) if len(l) > 1 else 0
                r = int(r1 + (r2 - r1) * rt)
                g = int(g1 + (g2 - g1) * rt)
                b = int(b1 + (b2 - b1) * rt)
                cl += f"\033[38;2;{r};{g};{b}m{c}"
            gt.append(cl + "\033[0m")
    else:
        for i, l in enumerate(ls):
            rt = i / len(ls) if len(ls) > 1 else 0
            r = int(r1 + (r2 - r1) * rt)
            g = int(g1 + (g2 - g1) * rt)
            b = int(b1 + (b2 - b1) * rt)
            gt.append(f"\033[38;2;{r};{g};{b}m{l}\033[0m")

    res = '\n'.join(gt)
    print(res)
    return res


def animate(text, at='typing', s=0.1):
    if at == 'typing':
        for c in text:
            print(c, end='', flush=True)
            time.sleep(s)
        print()
    elif at == 'fade':
        for _ in range(3):
            print(text, end='\r', flush=True)
            time.sleep(s)
            print(' ' * len(text), end='\r', flush=True)
            time.sleep(s)
        print(text)


def frame(text, s='single'):
    st = {
        'single': ('┌', '┐', '└', '┘', '─', '│'),
        'double': ('╔', '╗', '╚', '╝', '═', '║'),
        'dots': ('·', '·', '·', '·', '·', '·')
    }

    t, tr, b, br, h, v = st.get(s, st['single'])
    ls = text.split('\n')
    w = max(len(l) for l in ls) + 2

    tp = t + h * (w - 2) + tr
    bt = b + h * (w - 2) + br

    res = [tp]
    for l in ls:
        res.append(f"{v} {l:<{w - 2}} {v}")
    res.append(bt)

    print('\n'.join(res))
    return '\n'.join(res)


def center(text):
    tw = shutil.get_terminal_size().columns
    ls = text.split('\n')
    cl = [l.center(tw) for l in ls]
    res = '\n'.join(cl)
    print(res)
    return res


def table(data: List[Dict[str, Any]], headers: List[str] = None):
    if not data:
        return

    if not headers:
        headers = list(data[0].keys())

    cw = {h: len(h) for h in headers}
    for r in data:
        for h in headers:
            w = len(str(r.get(h, '')))
            cw[h] = max(cw[h], w)

    sep = '+' + '+'.join('-' * (cw[h] + 2) for h in headers) + '+'

    res = [sep]
    hl = '|'
    for h in headers:
        hl += f' {h:<{cw[h]}} |'
    res.append(hl)
    res.append(sep)

    for r in data:
        dl = '|'
        for h in headers:
            dl += f' {str(r.get(h, "")):<{cw[h]}} |'
        res.append(dl)

    res.append(sep)
    print('\n'.join(res))
    return '\n'.join(res)


def progress(current, total, w=50):
    p = current / total
    f = int(w * p)
    b = '█' * f + '░' * (w - f)
    pc = int(p * 100)
    print(f'\rProgress: |{b}| {pc}%', end='', flush=True)
    if current == total:
        print()


def convert(number, frm='10', to='2'):
    bases = {
        '2': 2,
        '8': 8,
        '10': 10,
        '16': 16
    }

    subscript = {
        '0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄',
        '5': '₅', '6': '₆', '7': '₇', '8': '₈', '9': '₉',
        '10': '₁₀', '16': '₁₆'
    }

    if frm == '10':
        decimal = int(number)
    else:
        decimal = int(str(number), bases[frm])

    if to == '2':
        result = bin(decimal)[2:]
    elif to == '8':
        result = oct(decimal)[2:]
    elif to == '16':
        result = hex(decimal)[2:]
    else:
        result = str(decimal)

    print(f"{number}{subscript[frm]} = {result}{subscript[to]}")
    return result
