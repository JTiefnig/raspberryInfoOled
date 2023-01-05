#!/usr/bin/env python
import psutil
import netifaces as ni
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
    ip = "not connected"
    ssid = ""

    try:
        ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
        ssid = ni.ifaddresses('wlan0')[ni.AF_INET][0]['broadcast']
    except:
        pass

    cpu = psutil.cpu_percent()

    cpu_temp = psutil.sensors_temperatures()
    cpu_temp = cpu_temp['cpu_thermal'][0][1]

    # get date and time from datetime DD-MM-YYYY HH:MN
    stringtime = datetime.now().strftime("%d-%m-%Y %H:%M")

    # get the percentage of the year that has passed
    date = datetime.now()
    startofyear = datetime(date.year, 1, 1)
    endofyear = datetime(date.year + 1, 1, 1)
    yearprogress = (date - startofyear) / (endofyear - startofyear)
    # rount to 2 decimal places
    yearprogress = round(yearprogress * 100, 2)
    yearprogress = str(yearprogress) + '%'

    # USE oled.text("Hello {}".format(i), 1) function to print out information
    oled.text(stringtime, 1)
    oled.text(ssid, 2)
    oled.text("IP:" + ip, 3)
    # print cpu usage and cpu temp and round to 1 decimal place
    oled.text("CPU:" + str(round(cpu, 1)) + "% " +
              str(round(cpu_temp, 1)) + "C", 4)
    oled.text(yearprogress, 5)
    sleep(5)
