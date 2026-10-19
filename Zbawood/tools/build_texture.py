# Texture generator for the Zbawood Glider item texture
# Requires Pillow: pip install pillow
from PIL import Image
import os

W, H = 32, 32
img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
px = img.load()

# Simple 16x16 pattern scaled 2x and centered
pattern = [
"0000333300000000",
"0033333333000000",
"0333111133300000",
"0331111113330000",
"0311111111133000",
"0311111111113000",
"0311111111113000",
"0311111111113000",
"0311111111113000",
"0311111111113000",
"0331111111133000",
"0333111113330000",
"0033333333000000",
"0003333330000000",
"0000333300000000",
"0000000000000000",
]

palette = {
    "0": (0,0,0,0),
    "1": (12,12,12,255),
    "2": (60,60,60,255),
    "3": (200,0,200,255),
    "4": (255,255,255,255)
}

pattern = [line.ljust(16, '0')[:16] for line in pattern]

for y in range(16):
    for x in range(16):
        ch = pattern[y][x]
        color = palette.get(ch, (0,0,0,0))
        for dy in range(2):
            for dx in range(2):
                px[x*2+dx, y*2+dy] = color

outdir = os.path.join("Zbawood","resource_pack","textures","items")
os.makedirs(outdir, exist_ok=True)
img.save(os.path.join(outdir, "wooden_glider.png"))
print("Saved:", os.path.join(outdir, "wooden_glider.png"))
