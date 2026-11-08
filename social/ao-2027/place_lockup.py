"""Place the official AO Travel & Experiences x DAYS lockup on the Post 2 cover.

The lockup is taken pixel-for-pixel from the AO-approved cover (approved/AO27-cover.webp):
same pixels, same size, same position. No redrawing, recolouring, scaling or background
removal. The cover is rendered at the approved assets' size (1485x1856) so the lockup
lands exactly where it sits on the approved cover. The crop's edges are pure black
(max RGB 2), and the cover's top band is black, so the join is invisible.
Usage: python3 place_lockup.py <cover.png>
"""
import sys
from PIL import Image

SRC = 'approved/AO27-cover.webp'
BOX = (310, 120, 1132, 288)  # lockup plus a black margin, in approved-asset pixels

src = Image.open(SRC).convert('RGB')
cover = Image.open(sys.argv[1]).convert('RGB')
assert src.size == cover.size == (1485, 1856), (src.size, cover.size)
cover.paste(src.crop(BOX), BOX[:2])
cover.save(sys.argv[1])
