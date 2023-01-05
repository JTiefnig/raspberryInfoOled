from oled_text import OledText
import busio
from board import SCL, SDA
from time import sleep

from oled_text import OledText, Layout64, BigLine, SmallLine

i2c = busio.I2C(SCL, SDA)
oled = OledText(i2c, 128, 64)

# Write to the oled

for i in range(0, 10):

    oled.text("Hello {}".format(i), 1)  # Line 1

    # wait half a second

    sleep(0.5)
