"""Wipe the old copy off the five original slides so new text can be set on them.
Usage: python3 clean.py <orig_dir> <out_dir>
fill:    rectangles on flat background, repainted solid in the slide colour
inpaint: rectangles where text overlaps lines/photo; only the letter pixels are removed"""
import sys, cv2, numpy as np
from pathlib import Path
src, out = Path(sys.argv[1]), Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
RED, YEL = (58, 28, 235), (155, 244, 254)          # BGR

SLIDES = {
    # name: (file, bg, fill rects (x0,y0,x1,y1), inpaint jobs (rect, kind))
    "s1-cover": ("15.jpg", RED, [], [((250, 1770, 1400, 1832), "photo")]),
    "s2-days":  ("14.jpg", YEL, [(60, 1130, 1560, 1950)], []),
    "s3-hotel": ("11.jpg", RED, [(60, 1330, 1560, 1950)], []),
    "s4-nights": ("12.jpg", YEL, [(80, 370, 1560, 600), (820, 720, 1560, 1320)], []),
    "s5-escape": ("13.jpg", RED, [(150, 1630, 1450, 1900)], []),
}

def yellowish(roi):
    return (roi[..., 2] > 190) & (roi[..., 1] > 190) & (roi[..., 0] > 90)

def letter_mask(img, rect, kind):
    """Mask of letter pixels to inpaint (used where text sits over the photo)."""
    x0, y0, x1, y1 = rect
    roi = img[y0:y1, x0:x1].astype(int)
    m = yellowish(roi).astype(np.uint8) * 255
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((4, 4), np.uint8))   # drop 2-3px lines
    m = cv2.dilate(m, np.ones((7, 7), np.uint8))
    full = np.zeros(img.shape[:2], np.uint8); full[y0:y1, x0:x1] = m
    return full

def flat_keep_lines(img, rect, bg, keep_text=False):
    """Repaint a flat-colour strip solid, keeping thin cream lines (and, with keep_text,
    any large pale lettering such as the 'Bangkok' script)."""
    x0, y0, x1, y1 = rect
    roi = img[y0:y1, x0:x1]
    pale = yellowish(roi.astype(int)).astype(np.uint8)
    thick = cv2.morphologyEx(pale, cv2.MORPH_OPEN, np.ones((4, 4), np.uint8))
    keep = pale if keep_text else (pale & (1 - cv2.dilate(thick, np.ones((5, 5), np.uint8))))
    keep = cv2.dilate(keep, np.ones((2, 2), np.uint8)).astype(bool)
    out = np.empty_like(roi); out[:] = bg
    out[keep] = roi[keep]
    img[y0:y1, x0:x1] = out

for name, (f, bg, fills, jobs) in SLIDES.items():
    img = cv2.imread(str(src / f))
    for x0, y0, x1, y1 in fills:
        img[y0:y1, x0:x1] = bg
    if name == "s1-cover":
        flat_keep_lines(img, (300, 585, 1260, 700), bg, keep_text=True)   # 'AFTER DARK' band
        flat_keep_lines(img, (250, 1834, 1400, 1900), bg)                 # bottom red band
    if jobs:
        mask = np.zeros(img.shape[:2], np.uint8)
        for rect, kind in jobs:
            mask |= letter_mask(img, rect, kind)
        img = cv2.inpaint(img, mask, 6, cv2.INPAINT_TELEA)
    cv2.imwrite(str(out / f"{name}.png"), img)
    print("ok", name)
