# Write your code here :-)

# Write your code here :-)
# Vikram Anantha
# Aug 2 2023
# Auto-ID Lab Summer 2023 Internship

# Displaying headlights

## Imports ##

import time
import board
import neopixel
import displayio
import terminalio
from adafruit_display_text.label import Label
from adafruit_bitmap_font import bitmap_font
from adafruit_matrixportal.network import Network
from adafruit_matrixportal.matrix import Matrix

## Changable Vars ##

PATTERN = [1,1,1,0,0,1,0,1,0,0] # Sequence to display headlights (0 for off, 1 for on)
CAMERA_FPS = 2 # frame rate of the camera (determines speed of the pattern)
NYQ_COEF = 2 # Nyq's theorm says "at LEAST 2x the camera fps" so if we want to do more we can
OFF_COLOR = 0x000000
ON_COLOR  = 0xFFFF00
HLW = 25 # headlights width
HLH = 8 # headlights height
PADDINGLR = 5 # padding from the left (or right)

## Main function ##

def main():

    # --- Display setup ---
    matrix = Matrix()
    display = matrix.display
    network = Network(status_neopixel=board.NEOPIXEL, debug=False)

    # --- Drawing setup ---
    group = displayio.Group()  # Create a Group
    bitmap = displayio.Bitmap(64, 32, 8)  # Create a bitmap object,width, height, bit depth
    bitcolor = displayio.Palette(2)  # Create a color palette
    bitcolor[0] = OFF_COLOR  # black background
    bitcolor[1] = ON_COLOR  # white

    yTL = int((32-HLH)/2)
    xTL = PADDINGLR


    def display_headlights(onoff=1):
        # on = 1, off = 0
        for row in range(HLH):
            for col in range(HLW):
                bitmap[col+xTL, row + yTL] = onoff
                bitmap[64-(col+xTL), row + yTL] = onoff


    display_headlights()
    # Create a TileGrid using the Bitmap and Palette
    tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitcolor)
    group.append(tile_grid)  # Add the TileGrid to the Group

    # Display the group on the screen
    display.show(group)

    while True:
        for pattind, patt in enumerate(PATTERN):
            display_headlights(patt)
            time.sleep((1/CAMERA_FPS) * NYQ_COEF)
