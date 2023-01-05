# Basic I2C OLED that displays helpful information from your Raspberry Pi
## Please feel free to fork, copy, adapt if you find it useable

## Usage

### Enable I2C
```
sudo raspi-config
```
- Select 5 Interfacing Options
- Select P5 I2C
- Select Yes
- Select Ok
- Select Finish

### Reboot
```
sudo reboot
```

### Install OLED Python Library
```
sudo apt-get install python-smbus
sudo apt-get install python-pip
sudo pip install RPi.GPIO
sudo pip install Adafruit_SSD1306
```


### Configure Pi to Run Script on Boot
```
sudo nano /etc/rc.local
```
- Add the following line before the exit 0 line
```
sudo python /home/pi/raspberryInfoOled/info_display.py &
```
- Press CTRL+X to exit
- Press Y to save
- Press Enter to confirm the file name

### Reboot
```
sudo reboot
```

Happy Debugging!



