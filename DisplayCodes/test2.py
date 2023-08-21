import time
import board
import neopixel
import displayio
import terminalio
from adafruit_display_text.label import Label
from adafruit_bitmap_font import bitmap_font
from adafruit_matrixportal.network import Network
from adafruit_matrixportal.matrix import Matrix

def main():

    # --- Display setup ---
    matrix = Matrix()
    display = matrix.display
    network = Network(status_neopixel=board.NEOPIXEL, debug=False)

    # --- Drawing setup ---
    group = displayio.Group()  # Create a Group
    bitmap = displayio.Bitmap(64, 32, 8)  # Create a bitmap object,width, height, bit depth
    color = displayio.Palette(2)  # Create a color palette
    color[0] = 0x000000  # black background
    color[1] = 0xFF0000  # red

    start_points = [(20, 4), (20, 17), (34, 4), (34, 17)]
    boundary_x = [16, 47]

    fill_idx_1 = [0,0,1,0]
    fill_idx_2 = [0,1,1,0]
    fill_idx_3 = [0,0,1,0]
    fill_idx_4 = [0,0,0,0]
    fill_idx_5 = [1,0,1,1]
    fill_idx_6 = [1,1,1,1]
    fill_idx_7 = [1,0,1,0]
    fill_idx_8 = [0,0,1,0]
    fill_idx_9 = [1,1,1,1]
    fill_idx_10 = [1,0,0,0]

    def draw_output(points, boundary, idx, sz):
        for i in range(len(idx)):
            draw_outline(points[i][0], points[i][1], sz)
            if idx[i]:
                fill_box(points[i][0], points[i][1], sz)
        for j in range(32):
            bitmap[boundary[0],j] = 1
            bitmap[boundary[0]+1,j] = 1
            bitmap[boundary[1],j] = 1
            bitmap[boundary[1]+1,j] = 1

        for w in range(boundary[1]-boundary[0]):
            bitmap[boundary[0]+w, 0] = 1
            bitmap[boundary[0]+w, 1] = 1
            bitmap[boundary[0]+w, 30] = 1
            bitmap[boundary[0]+w, 31] = 1

    def draw_outline(start_x, start_y, size):
        for left in range(size):
            bitmap[start_x,start_y+left] = 1
        for right in range(size):
            bitmap[start_x+size,start_y+right] = 1
        for top in range(size):
            bitmap[start_x+top,start_y] = 1
        for bottom in range(size+1):
            bitmap[start_x+bottom,start_y+size] = 1


    def fill_box(x, y, dim):
        for i in range(dim):
            for j in range(dim):
                bitmap[x+i,y+j] = 1


    #draw_outline(10, 10, 10)
    #fill_box(10, 10, 10)
    draw_output(start_points, boundary_x, fill_idx_5, 10)

    # Create a TileGrid using the Bitmap and Palette
    tile_grid = displayio.TileGrid(bitmap, pixel_shader=color)
    group.append(tile_grid)  # Add the TileGrid to the Group

    # Display the group on the screen
    display.show(group)

    while True:
        time.sleep(1)

