"""Remove black body text from a poster's flat colour info panel (everything below y0),
keeping the panel colour and any light lettering/lines on it.
Usage: python3 clean_panel.py <in.jpg> <out.png> <y0_px> [keep_x0,keep_y0,keep_x1,keep_y1]"""
import sys, cv2, numpy as np
img = cv2.imread(sys.argv[1])
h, w = img.shape[:2]
y0 = int(sys.argv[3])                                # top of the info panel
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
dark = (hsv[..., 2] < 200).astype(np.uint8) * 255    # black text + its anti-aliased edge
dark[:y0] = 0
mask = cv2.dilate(dark, np.ones((5, 5), np.uint8))
out = cv2.inpaint(img, mask, 4, cv2.INPAINT_TELEA)
# The panel is one flat colour: repaint it solid to kill inpainting ghosts, except in
# an optional keep-box (x0,y0,x1,y1) where light graphic lines cross into the panel.
if len(sys.argv) > 4:
    flat = np.median(img[h - 40:h - 10, 20:200].reshape(-1, 3), axis=0).astype(np.uint8)
    keep = [int(v) for v in sys.argv[4].split(",")]
    region = np.zeros(img.shape[:2], bool); region[y0:] = True
    region[keep[1]:keep[3], keep[0]:keep[2]] = False
    out[region] = flat
cv2.imwrite(sys.argv[2], out)
print("ok", int(mask.sum() / 255), "px")
