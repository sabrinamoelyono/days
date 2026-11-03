"""Remove baked-in text from the old visa posts so the photos can be reused.
Usage: python3 clean_plates.py <source_images_dir> <out_dir>"""
import sys, cv2, numpy as np
from pathlib import Path
src, out = Path(sys.argv[1]), Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)

def textmask(img, rect, thr=28, grow=11):
    x0,y0,x1,y1 = rect
    roi = img[y0:y1, x0:x1]
    bg = cv2.medianBlur(roi, 41)
    d = cv2.absdiff(roi, bg).max(axis=2)
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    # sky is pale and unsaturated; anything else in a text rect is lettering
    m = ((d > thr) | (hsv[...,1] > 45) | (hsv[...,2] < 165)).astype(np.uint8)*255
    m = cv2.dilate(m, np.ones((grow,grow),np.uint8))
    full = np.zeros(img.shape[:2], np.uint8); full[y0:y1, x0:x1] = m
    return full

def box(img, rect):
    m = np.zeros(img.shape[:2], np.uint8); x0,y0,x1,y1 = rect; m[y0:y1,x0:x1]=255; return m

jobs = {
  # file: (soft text rects over smooth sky, hard rects over texture)
  '1.jpg': ([(405,100,1000,368),(492,368,1000,475),(425,380,492,440),(425,440,468,453),(455,418,494,449)], [(412,370,500,381),(412,370,425,468),(412,456,500,468)]),
  '2.jpg': ([(85,80,880,250),(85,250,640,385),(640,236,857,276)], []),
  '4.jpg': ([], [(320,80,580,160)]),
}
for name,(soft,hard) in jobs.items():
    img = cv2.imread(str(src/name))
    m = np.zeros(img.shape[:2], np.uint8)
    for r in soft: m |= textmask(img, r)
    for r in hard: m |= box(img, r)
    res = cv2.inpaint(img, m, 9, cv2.INPAINT_TELEA)
    cv2.imwrite(str(out/('clean-'+name)), res, [cv2.IMWRITE_JPEG_QUALITY, 95])
    print('ok', name)

# Final plates: crop away the old CTA/logo areas that inpainting can't rebuild well.
crops = {
    'plate-china.jpg':     ('clean-1.jpg', (0, 0, 1080, 838)),
    'plate-schengen.jpg':  ('clean-2.jpg', (0, 0, 1080, 838)),
    'plate-pisa-tall.jpg': ('clean-2.jpg', (380, 150, 1080, 838)),
    'plate-panda.jpg':     ('clean-4.jpg', (0, 0, 900, 925)),
}
for name, (f, (x0, y0, x1, y1)) in crops.items():
    img = cv2.imread(str(out/f))[y0:y1, x0:x1]
    cv2.imwrite(str(out/name), img, [cv2.IMWRITE_JPEG_QUALITY, 95])
    print('ok', name)
