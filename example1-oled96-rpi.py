#!/usr/bin/env python

from PIL import ImageFont
from lib_oled96 import ssd1306

from smbus import SMBus
i2cbus = SMBus(1)        # 1 = Raspberry Pi but NOT early REV1 board
# create oled object, nominating the correct I2C bus, default address
oled = ssd1306(i2cbus)

# we are ready to do some output ...


font = ImageFont.load_default()  # truetype('FreeMono.ttf', 8)
# Write two lines of text.
oled.canvas.text((40, 15),    'Hello', font=font, fill=1)
oled.canvas.text((40, 40),    'World!', fill=1)

# now display that canvas out to the hardware
oled.display()
