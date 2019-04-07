# sys status
Show system status of Raspberry Pi in a PCD8544 screen
![alt text](src/demo.png)

# Dependency
1. sudo pip3 install -r requirements.txt
2. install `Adafruit_Nokia_LCD`
```
git clone https://github.com/adafruit/Adafruit_Nokia_LCD.git
cd Adafruit_Nokia_LCD
sudo python3 setup.py install
```

## Usage
1. Edit `screen_config.ini` if needed
2. Kick off `sys_status.py`

## Other options
- Use `image_generate.py` to preview the image before sending to Raspberry Pi
- Adjust `sys_status.py` to get inverted color
