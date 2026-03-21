import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.peg_oled_Display import Oled, OledDisplayMode, OledReactionType, OledData
from kmk.extensions.RGB import RGB

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

# 📍 YOUR MATRIX PINS (Mapped directly from your KiCad Schematic)
# Columns connect to D0, D1, D2, D3
keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3)
# Rows connect to D7, D6, D9, D10
keyboard.row_pins = (board.D7, board.D6, board.D9, board.D10)
# Diodes point from switches to the rows
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# 🌈 YOUR RGB LED SETUP (Wired to pin D8)
# This turns on the 16 SK6812MINI LEDs at 20% brightness
rgb = RGB(pixel_pin=board.D8, num_pixels=16, val_limit=100, hue_default=0, sat_default=255, val_default=20)
keyboard.extensions.append(rgb)

# 📺 YOUR OLED SETUP (Wired to D4 for SDA, D5 for SCL)
oled_ext = Oled(
    OledData(
        corner_one={0:OledReactionType.STATIC, 1:["Nexus16"]},
        corner_two={0:OledReactionType.LAYER, 1:["Layer 1"]},
        corner_three={0:OledReactionType.STATIC, 1:["SYSTEM"]},
        corner_four={0:OledReactionType.STATIC, 1:["ONLINE"]}
    ),
    toDisplay=OledDisplayMode.TXT,
    flip=False
)
keyboard.extensions.append(oled_ext)

# ⌨️ YOUR KEYMAP (How the buttons work)
keyboard.keymap = [
    [
        KC.N7, KC.N8, KC.N9, KC.BSPC,  # Row 1 (Top)
        KC.N4, KC.N5, KC.N6, KC.ENTER, # Row 2
        KC.N1, KC.N2, KC.N3, KC.UP,    # Row 3
        KC.N0, KC.DOT, KC.LEFT, KC.RIGHT # Row 4 (Bottom)
    ]
]

if __name__ == '__main__':
    keyboard.go()