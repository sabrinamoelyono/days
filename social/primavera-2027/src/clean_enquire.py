"""Remove the black body text from the Enquire Now poster, keeping pink bg + yellow headers.
Usage: python3 clean_enquire.py <in.jpg> <out.png>"""
import sys, cv2, numpy as np
img = cv2.imread(sys.argv[1])
h, w = img.shape[:2]
y0 = int(h * 0.70)                                   # pink info panel only
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
dark = (hsv[..., 2] < 200).astype(np.uint8) * 255    # black text + its anti-aliased edge
dark[:y0] = 0
mask = cv2.dilate(dark, np.ones((5, 5), np.uint8))
out = cv2.inpaint(img, mask, 4, cv2.INPAINT_TELEA)
cv2.imwrite(sys.argv[2], out)
print("ok", int(mask.sum() / 255), "px")
