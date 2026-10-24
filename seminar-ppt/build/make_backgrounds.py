"""Generate the glow backgrounds for Utkarsh's dark deck (4:3, 2000x1500)."""
import sys

from PIL import Image, ImageDraw, ImageFilter

W, H = 2000, 1500
BASE = (11, 16, 32)


def glow(img, cx, cy, r, color, alpha):
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(layer).ellipse([cx - r, cy - r, cx + r, cy + r], fill=color + (alpha,))
    layer = layer.filter(ImageFilter.GaussianBlur(r * 0.45))
    img.alpha_composite(layer)


def dots(img, step, alpha):
    d = ImageDraw.Draw(img)
    for x in range(step // 2, W, step):
        for y in range(step // 2, H, step):
            d.ellipse([x - 2, y - 2, x + 2, y + 2], fill=(160, 175, 230, alpha))


out = sys.argv[1]
cover = Image.new("RGBA", (W, H), BASE + (255,))
dots(cover, 60, 14)
glow(cover, 1650, 650, 620, (124, 58, 237), 150)
glow(cover, 250, 1400, 560, (6, 182, 212), 95)
cover.convert("RGB").save(f"{out}/bg_cover.jpg", quality=92)

content = Image.new("RGBA", (W, H), BASE + (255,))
glow(content, 1900, 60, 520, (124, 58, 237), 70)
glow(content, 80, 1480, 480, (6, 182, 212), 45)
content.convert("RGB").save(f"{out}/bg_content.jpg", quality=92)
print("ok")
