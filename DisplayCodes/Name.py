# Write your code here :-)
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
    BLINK = True
    DEBUG = False

    # Get wifi details and more from a secrets.py file
    try:
        from secrets import secrets
    except ImportError:
        print("WiFi secrets are kept in secrets.py, please add them there!")
        raise
    print("    My Name Display")
    print("Name will be set for {}".format(secrets["timezone"]))

    # --- Display setup ---
    matrix = Matrix()
    display = matrix.display
    network = Network(status_neopixel=board.NEOPIXEL, debug=False)

    # --- Drawing setup ---
    group = displayio.Group()  # Create a Group
    bitmap = displayio.Bitmap(64, 32, 2)  # Create a bitmap object,width, height, bit depth
    color = displayio.Palette(4)  # Create a color palette
    color[0] = 0x000000  # black background
    color[1] = 0xFF0000  # red
    color[2] = 0xCC4000  # amber
    color[3] = 0x85FF00  # greenish

    # Create a TileGrid using the Bitmap and Palette
    tile_grid = displayio.TileGrid(bitmap, pixel_shader=color)
    group.append(tile_grid)  # Add the TileGrid to the Group
    display.show(group)

    if not DEBUG:
        font = bitmap_font.load_font("/IBMPlexMono-Medium-24_jep.bdf")
    else:
        font = terminalio.FONT

    name_label = Label(font)


    def update_name():
        name_label.text = "Ben" # Replace "Your Name" with your actual name
        bbx, bby, bbwidth, bbh = name_label.bounding_box
        # Center the label
        name_label.x = round(display.width / 2 - bbwidth / 2)
        name_label.y = display.height // 2
        if DEBUG:
            print("Label bounding box: {},{},{},{}".format(bbx, bby, bbwidth, bbh))
            print("Label x: {} y: {}".format(name_label.x, name_label.y))


    last_check = None
    update_name()  # Display your name on the board
    group.append(name_label)  # add the name label to the group

    while True:
        if last_check is None or time.monotonic() > last_check + 3600:
            try:
                network.get_local_time()  # Synchronize Board's clock to Internet
                last_check = time.monotonic()
            except RuntimeError as e:
                print("Some error occured, retrying! -", e)

        update_name()
        time.sleep(1)
