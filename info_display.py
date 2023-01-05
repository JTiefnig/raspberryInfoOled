#!/usr/bin/env python
import subprocess
from time import sleep
from datetime import datetime
import busio
from board import SCL, SDA
from oled_text import OledText, Layout64, BigLine, SmallLine

i2c = busio.I2C(SCL, SDA)
oled = OledText(i2c, 128, 64)

# loop every 5 seconds
while True:

    # get wifi info
    # get ip address
    ip = subprocess.check_output(['hostname', '-I'])
    ip = ip.decode("utf-8")
    # get ssid
    ssid = subprocess.check_output(['iwgetid', '-r'])
    ssid = ssid.decode("utf-8")

    # get cpu info
    # get cpu temperature
    cputemp = subprocess.check_output(['vcgencmd', 'measure_temp'])
    cputemp = cputemp.decode("utf-8")
    cputemp = cputemp[5:9] + 'C'
    # get cpu usage
    cpu = subprocess.check_output(['top', '-bn1'])
    cpu = cpu.decode("utf-8")
    cpu = cpu[cpu.find('Cpu(s):')+7:cpu.find('Cpu(s):')+12] + '%'

    # get date time in format: 2019-01-01 00:00:00
    stringtime = subprocess.check_output(['date', '+%Y-%m-%d %H:%M'])
    stringtime = stringtime.decode("utf-8")

    # get the percentage of the year that has passed
    date = datetime.now()
    startofyear = datetime(date.year, 1, 1)
    endofyear = datetime(date.year + 1, 1, 1)
    yearprogress = (date - startofyear) / (endofyear - startofyear)
    # rount to 2 decimal places
    yearprogress = round(yearprogress * 100, 2)
    yearprogress = str(yearprogress) + '%'

    # get hostname
    hostname = subprocess.check_output(['hostname'])
    hostname = hostname.decode("utf-8")

    # USE oled.text("Hello {}".format(i), 1) function to print out information
    oled.text(stringtime, 1)
    oled.text(ssid, 2)
    oled.text("IP:" + ip, 3)
    oled.text("CPU:" + cpu + " " + cputemp, 4)
    oled.text(yearprogress, 5)
    sleep(5)
