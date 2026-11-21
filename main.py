#!/usr/bin/env python3
"""VELMARIS - The Poster for a Place That Isn't There.

A travel poster for an invented place, drawn procedurally with the Python
standard library only (no PIL, no network, no fonts on disk). The program
renders a 1024x1024 PNG and writes it to /output/entry.png (or argv[1]).

The place: VELMARIS - a cliff town where waterfalls pour from islands that
float in a violet dusk sky into a turquoise sea, watched over by a lighthouse
on a needle rock. The name is set in large hand-built vector capitals; no
other copy appears anywhere on the poster.

Deterministic: every pixel is a pure function of fixed constants, so two
runs produce byte-identical output.
"""

import math
import struct
import sys
import zlib

W = 1024
H = 1024

# ---------------------------------------------------------------- palette ---
INK = (16, 22, 43)          # deep silhouette indigo
CREAM = (247, 234, 208)      # title cream
SUN_CORE = (255, 217, 138)
SUN_GLOW = (255, 178, 102)
PEACH = (240, 138, 99)
MAUVE = (156, 85, 120)
PURPLE = (67, 41, 94)
INDIGO = (23, 28, 56)
SEA_TOP = (42, 127, 140)
SEA_BOT = (18, 63, 82)
FOAM = (207, 232, 239)
LAMP = (255, 196, 110)


def lerp(a, b, t):
    return a + (b - a) * t


def mix(c1, c2, t):
    return (int(lerp(c1[0], c2[0], t)),
            int(lerp(c1[1], c2[1], t)),
            int(lerp(c1[2], c2[2], t)))


def clamp(v, lo, hi):
    return lo if v < lo else hi if v > hi else v


class Canvas:
    """A plain RGB pixel buffer with small drawing helpers."""

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.px = bytearray(w * h * 3)

    def set(self, x, y, color):
        x = int(x)
        y = int(y)
        if 0 <= x < self.w and 0 <= y < self.h:
            i = (y * self.w + x) * 3
            self.px[i] = color[0]
            self.px[i + 1] = color[1]
            self.px[i + 2] = color[2]

    def blend(self, x, y, color, alpha):
        """Blend color over the pixel at (x, y); alpha in [0, 1]."""
        x = int(x)
        y = int(y)
        if alpha <= 0 or not (0 <= x < self.w and 0 <= y < self.h):
            return
        if alpha >= 1:
            self.set(x, y, color)
            return
        i = (y * self.w + x) * 3
        self.px[i] = int(self.px[i] + (color[0] - self.px[i]) * alpha)
        self.px[i + 1] = int(self.px[i + 1] + (color[1] - self.px[i + 1]) * alpha)
        self.px[i + 2] = int(self.px[i + 2] + (color[2] - self.px[i + 2]) * alpha)

    def get(self, x, y):
        x = int(clamp(x, 0, self.w - 1))
        y = int(clamp(y, 0, self.h - 1))
        i = (y * self.w + x) * 3
        return (self.px[i], self.px[i + 1], self.px[i + 2])

    def vgrad(self, y0, y1, stops):
        """Vertical gradient; stops = [(pos 0..1, color), ...] sorted."""
        for y in range(max(0, y0), min(self.h, y1)):
            t = (y - y0) / max(1, (y1 - y0))
            for j in range(len(stops) - 1):
                p0, c0 = stops[j]
                p1, c1 = stops[j + 1]
                if p0 <= t <= p1:
                    u = 0 if p1 == p0 else (t - p0) / (p1 - p0)
                    col = mix(c0, c1, u)
                    break
            else:
                col = stops[-1][1]
            i = (y * self.w) * 3
            for x in range(self.w):
                self.px[i] = col[0]
                self.px[i + 1] = col[1]
                self.px[i + 2] = col[2]
                i += 3

    def disc(self, cx, cy, r, color, alpha=1.0):
        r = int(r)
        for y in range(int(cy - r), int(cy + r) + 1):
            dx = int(math.sqrt(max(0, r * r - (y - cy) ** 2)))
            for x in range(int(cx - dx), int(cx + dx) + 1):
                self.blend(x, y, color, alpha)

    def hline(self, x0, x1, y, color, alpha=1.0):
        for x in range(int(x0), int(x1) + 1):
            self.blend(x, y, color, alpha)

    def line(self, x0, y0, x1, y1, width, color, alpha=1.0):
        """Thick line with round caps, drawn as a chain of discs."""
        dx = x1 - x0
        dy = y1 - y0
        dist = math.hypot(dx, dy)
        steps = max(1, int(dist))
        r = max(1.0, width / 2.0)
        for s in range(steps + 1):
            t = s / steps
            self.disc(x0 + dx * t, y0 + dy * t, r, color, alpha)

    def poly(self, points, color, alpha=1.0):
        """Scanline-filled polygon; points = [(x, y), ...]."""
        if len(points) < 3:
            return
        ys = [p[1] for p in points]
        y_min = max(0, int(math.floor(min(ys))))
        y_max = min(self.h - 1, int(math.ceil(max(ys))))
        n = len(points)
        for y in range(y_min, y_max + 1):
            xs = []
            for k in range(n):
                x0, y0 = points[k]
                x1, y1 = points[(k + 1) % n]
                if (y0 <= y < y1) or (y1 <= y < y0):
                    t = (y - y0) / (y1 - y0)
                    xs.append(x0 + t * (x1 - x0))
            xs.sort()
            for j in range(0, len(xs) - 1, 2):
                self.hline(xs[j], xs[j + 1], y, color, alpha)

    def ellipse(self, cx, cy, rx, ry, color, alpha=1.0):
        for y in range(int(cy - ry), int(cy + ry) + 1):
            t = (y - cy) / ry
            if abs(t) > 1:
                continue
            dx = rx * math.sqrt(1 - t * t)
            self.hline(cx - dx, cx + dx, y, color, alpha)


# ------------------------------------------------------- deterministic noise --
def _lcg(seed):
    """Tiny deterministic pseudo-random stream (fixed seed -> fixed output)."""
    state = seed & 0xFFFFFFFF

    def nxt():
        nonlocal state
        state = (1664525 * state + 1013904223) & 0xFFFFFFFF
        return state / 4294967296.0

    return nxt


# ------------------------------------------------------------- vector type ---
# Hand-built single-stroke capitals on an 8 x 12 grid (y grows downward).
# Only the letters of VELMARIS are needed, which keeps the font honest.
FONT = {
    "V": [((0, 0), (4, 12)), ((4, 12), (8, 0))],
    "E": [((7, 0), (0, 0)), ((0, 0), (0, 12)), ((0, 12), (7, 12)),
          ((0, 6), (5, 6))],
    "L": [((0, 0), (0, 12)), ((0, 12), (7, 12))],
    "M": [((0, 12), (0, 0)), ((0, 0), (4, 7)), ((4, 7), (8, 0)),
          ((8, 0), (8, 12))],
    "A": [((0, 12), (4, 0)), ((4, 0), (8, 12)), ((2, 8), (6, 8))],
    "R": [((0, 12), (0, 0)), ((0, 0), (6, 0)), ((6, 0), (7, 2)),
          ((7, 2), (6, 4)), ((6, 4), (0, 4)), ((5, 4), (8, 12))],
    "I": [((2, 0), (6, 0)), ((4, 0), (4, 12)), ((2, 12), (6, 12))],
    "S": [((7, 2), (6, 0)), ((6, 0), (2, 0)), ((2, 0), (1, 2)),
          ((1, 2), (1, 4)), ((1, 4), (7, 8)), ((7, 8), (7, 10)),
          ((7, 10), (6, 12)), ((6, 12), (2, 12)), ((2, 12), (1, 10))],
}


def draw_text(cv, text, cx, top, height, color, weight=None, tracking=0.34):
    """Draw centred capitals; returns the width actually used."""
    if weight is None:
        weight = max(6.0, height * 0.085)
    unit_w = height * (8.0 / 12.0)
    gap = unit_w * tracking
    total = len(text) * unit_w + (len(text) - 1) * gap
    x = cx - total / 2.0
    sx = height / 12.0
    sy = height / 12.0
    for ch in text:
        for (ax, ay), (bx, by) in FONT.get(ch, []):
            cv.line(x + ax * sx, top + ay * sy,
                    x + bx * sx, top + by * sy,
                    weight, color)
        x += unit_w + gap
    return total


# ------------------------------------------------------------------- scene ---
HORIZON = 640
SUN = (648, 566)


def draw_sky(cv):
    cv.vgrad(0, HORIZON, [
        (0.00, INDIGO),
        (0.30, PURPLE),
        (0.52, MAUVE),
        (0.68, PEACH),
        (0.82, (247, 185, 106)),
        (1.00, (250, 205, 130)),
    ])
    # Stars, only in the deep upper sky, fixed seed -> fixed sky.
    rnd = _lcg(20261121)
    for _ in range(110):
        x = rnd() * W
        y = rnd() * 330
        a = 0.25 + 0.6 * rnd()
        r = 1.0 if rnd() < 0.85 else 1.8
        cv.disc(x, y, r, (255, 244, 214), a * (1 - y / 420.0))


def draw_sun(cv):
    cx, cy = SUN
    for r, a in ((250, 0.05), (200, 0.07), (160, 0.10), (125, 0.16)):
        cv.disc(cx, cy, r, SUN_GLOW, a)
    cv.disc(cx, cy, 96, SUN_CORE)
    cv.disc(cx, cy, 88, (255, 228, 160))
    # A thin bright rim where the sun meets the haze.
    for ang in range(0, 360, 2):
        t = math.radians(ang)
        cv.blend(cx + 96 * math.cos(t), cy + 96 * math.sin(t),
                 (255, 240, 200), 0.5)


def draw_island(cv, pts, rim, falls, top_x, top_y, tower=False):
    """A floating rock island with rim light and waterfalls off its edge."""
    cv.poly(pts, INK)
    # Warm rim light along the top edge.
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        if y1 <= y0 + 4 and y0 < 340:
            cv.line(x0, y0, x1, y1, 3, rim, 0.8)
    if tower:
        bx, by = top_x, top_y
        cv.poly([(bx - 16, by), (bx - 10, by - 46), (bx + 10, by - 46),
                 (bx + 16, by)], INK)
        cv.poly([(bx - 8, by - 46), (bx + 8, by - 46),
                 (bx + 4, by - 58), (bx - 4, by - 58)], INK)
        cv.disc(bx, by - 52, 3, LAMP)
    for fx in falls:
        base_y = max(p[1] for p in pts if abs(p[0] - fx) < 60)
        span = float(HORIZON - base_y + 1)
        for s in range(0, HORIZON - int(base_y), 3):
            y = base_y + s
            wob = 4 * math.sin(y / 26.0 + fx)
            a = 0.55 * (1 - s / span) + 0.15
            cv.line(fx + wob - 2, y, fx + wob + 2, y + 8, 4, FOAM, a * 0.7)
            cv.line(fx + wob - 1, y, fx + wob + 1, y + 8, 2, (240, 248, 250),
                    a * 0.9)
        cv.ellipse(fx, HORIZON - 4, 26, 7, FOAM, 0.35)


def draw_sea(cv):
    cv.vgrad(HORIZON, H, [
        (0.00, SEA_TOP),
        (0.45, (28, 102, 118)),
        (1.00, SEA_BOT),
    ])
    # Sun path: a shimmering column of gold under the sun.
    rnd = _lcg(77)
    for y in range(HORIZON + 6, H - 120, 9):
        spread = 26 + (y - HORIZON) * 0.42
        n = int(2 + (y - HORIZON) / 60)
        for _ in range(n):
            x = SUN[0] + (rnd() * 2 - 1) * spread
            ln = 14 + rnd() * 34
            a = 0.55 * (1 - (y - HORIZON) / 380.0) + 0.08
            cv.hline(x - ln / 2, x + ln / 2, y, (255, 214, 140), a)
    # Sparse wave dashes across the rest of the sea.
    rnd = _lcg(913)
    for _ in range(150):
        x = rnd() * W
        y = HORIZON + 14 + rnd() * (H - HORIZON - 150)
        ln = 8 + rnd() * 30
        cv.hline(x, x + ln, y, (140, 205, 205), 0.10 + 0.16 * rnd())


def draw_headland(cv):
    """Cliff town on the right, lighthouse on a needle rock, town lights."""
    cv.poly([(700, HORIZON), (760, 690), (830, 668), (900, 700),
             (960, 676), (1024, 700), (1024, H), (700, H)], INK)
    # Rooftops along the headland ridge.
    roofs = [(724, 690, 30), (772, 678, 24), (836, 672, 28), (884, 690, 22),
             (928, 684, 26), (972, 692, 24)]
    for rx, ry, rw in roofs:
        cv.poly([(rx, ry), (rx + rw / 2, ry - 16), (rx + rw, ry)], INK)
    # Warm windows.
    rnd = _lcg(4242)
    for _ in range(46):
        x = 706 + rnd() * 300
        y = 700 + rnd() * 120
        cv.set(x, y, LAMP)
        cv.set(x + 1, y, (255, 220, 150))
    # Lighthouse on its needle rock, left of the sun so its lamp glows
    # against the open sky, not inside the sun disc.
    lx = 530
    cv.poly([(lx - 24, HORIZON + 8), (lx - 8, 596), (lx + 8, 596),
             (lx + 24, HORIZON + 8)], INK)
    cv.poly([(lx - 8, 596), (lx - 4, 548), (lx + 4, 548), (lx + 8, 596)],
            (24, 30, 54))
    cv.poly([(lx - 10, 548), (lx + 10, 548), (lx + 6, 532), (lx - 6, 532)],
            INK)
    cv.disc(lx, 540, 5, LAMP)
    cv.disc(lx, 540, 16, LAMP, 0.35)
    cv.disc(lx, 540, 34, LAMP, 0.12)
    # The lamp's beam sweeping low over the water.
    cv.poly([(lx, 540), (1024, 600), (1024, 622), (lx, 548)],
            (255, 214, 140), 0.10)
    # Foreground cliff, bottom-left, with two cypress silhouettes.
    cv.poly([(0, H), (0, 930), (120, 900), (260, 940), (330, 1010),
             (330, H)], INK)
    for tx, th in ((96, 74), (150, 96), (205, 62)):
        cv.poly([(tx - 13, 936), (tx, 936 - th), (tx + 13, 936)], INK)
        cv.line(tx, 936, tx, 946, 5, INK)


def draw_birds(cv):
    for bx, by, s in ((300, 210, 12), (352, 188, 9), (420, 238, 11),
                      (760, 160, 10), (812, 196, 8), (880, 148, 12)):
        cv.line(bx - s, by, bx, by - s * 0.55, 2.5, INK, 0.9)
        cv.line(bx, by - s * 0.55, bx + s, by, 2.5, INK, 0.9)


def draw_title_band(cv):
    # A soft dark band grounds the title over the sea.
    for y in range(820, H):
        a = 0.55 * ((y - 820) / 204.0) ** 1.4
        for x in range(0, W, 1):
            cv.blend(x, y, (10, 14, 30), a * 0.55)
    cv.hline(212, 812, 856, CREAM, 0.65)
    draw_text(cv, "VELMARIS", 512, 876, 92, (12, 16, 34))
    draw_text(cv, "VELMARIS", 512, 872, 92, CREAM)
    cv.hline(212, 812, 986, CREAM, 0.65)


def render():
    cv = Canvas(W, H)
    draw_sky(cv)
    draw_sun(cv)
    # Two floating islands, waterfalls falling from them into the sea.
    draw_island(cv,
                [(150, 318), (470, 300), (500, 330), (430, 400),
                 (380, 428), (300, 412), (210, 430), (160, 360)],
                SUN_GLOW, [238, 330, 412], 300, 316, tower=True)
    draw_island(cv,
                [(700, 218), (880, 206), (912, 232), (860, 282),
                 (790, 296), (730, 272)], SUN_GLOW, [790, 852],
                800, 214, tower=False)
    draw_birds(cv)
    draw_sea(cv)
    draw_headland(cv)
    draw_title_band(cv)
    return cv


# ------------------------------------------------------------------ PNG out ---
def write_png(path, cv):
    raw = bytearray()
    for y in range(cv.h):
        raw.append(0)  # filter: none
        raw += cv.px[y * cv.w * 3:(y + 1) * cv.w * 3]
    comp = zlib.compress(bytes(raw), 9)

    def chunk(tag, data):
        out = struct.pack(">I", len(data)) + tag + data
        out += struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)
        return out

    png = b"\x89PNG\r\n\x1a\n"
    png += chunk(b"IHDR", struct.pack(">IIBBBBB", cv.w, cv.h, 8, 2, 0, 0, 0))
    png += chunk(b"IDAT", comp)
    png += chunk(b"IEND", b"")
    with open(path, "wb") as f:
        f.write(png)
    return len(png)


def validate_png_bytes(path, expect_w, expect_h):
    """Integrity check on the file just written: PNG signature, IHDR
    dimensions, IDAT decodes to exactly the expected raw scanlines, and
    the file fits the 1 MiB gate. Raises SystemExit on any mismatch so a
    corrupt render can never be mistaken for a valid entry."""
    with open(path, "rb") as f:
        data = f.read()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise SystemExit(f"INVALID: {path}: bad PNG signature")
    if len(data) > 1048576:
        raise SystemExit(f"INVALID: {path}: {len(data)} bytes > 1 MiB gate")
    pos = 8
    ihdr = None
    idat = bytearray()
    while pos < len(data):
        (length,) = struct.unpack(">I", data[pos:pos + 4])
        tag = data[pos + 4:pos + 8]
        payload = data[pos + 8:pos + 8 + length]
        (crc,) = struct.unpack(">I", data[pos + 8 + length:pos + 12 + length])
        if zlib.crc32(tag + payload) & 0xFFFFFFFF != crc:
            raise SystemExit(f"INVALID: {path}: bad CRC in {tag!r} chunk")
        if tag == b"IHDR":
            ihdr = struct.unpack(">IIBBBBB", payload)
        elif tag == b"IDAT":
            idat += payload
        pos += 12 + length
    if ihdr is None:
        raise SystemExit(f"INVALID: {path}: no IHDR chunk")
    w, h, depth, ctype, _, _, _ = ihdr
    if (w, h) != (expect_w, expect_h):
        raise SystemExit(f"INVALID: {path}: {w}x{h}, expected "
                         f"{expect_w}x{expect_h}")
    if depth != 8 or ctype != 2:
        raise SystemExit(f"INVALID: {path}: bit depth {depth}, colour "
                         f"type {ctype}, expected 8 / 2 (RGB)")
    raw = zlib.decompress(bytes(idat))
    if len(raw) != expect_h * (1 + expect_w * 3):
        raise SystemExit(f"INVALID: {path}: IDAT decodes to {len(raw)} "
                         f"bytes, expected {expect_h * (1 + expect_w * 3)}")
    if any(raw[y * (1 + expect_w * 3)] != 0 for y in range(expect_h)):
        raise SystemExit(f"INVALID: {path}: non-zero scanline filter byte")
    return len(data)


def main(argv):
    out = argv[1] if len(argv) > 1 else "/output/entry.png"
    # Determinism self-check: render twice in-process and require the
    # pixel buffers to be identical before anything is written. This
    # catches any future accidental nondeterminism (unseeded randomness,
    # dict/set iteration order, wall-clock use) at build time instead of
    # letting two grader runs disagree.
    cv = render()
    cv2 = render()
    if cv.px != cv2.px:
        diff = sum(1 for a, b in zip(cv.px, cv2.px) if a != b)
        raise SystemExit(f"NONDETERMINISTIC: two renders differ in "
                         f"{diff} bytes; refusing to write {out}")
    size = write_png(out, cv)
    validate_png_bytes(out, cv.w, cv.h)
    print(f"wrote {out} ({cv.w}x{cv.h}, {size} bytes)")


if __name__ == "__main__":
    main(sys.argv)
