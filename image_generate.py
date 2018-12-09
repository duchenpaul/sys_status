import os
import time
import socket
import psutil

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageOps

import toolkit_text
import logging_manager

LCDWIDTH, LCDHEIGHT = 84, 48


def get_CPU_temperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=", "").replace("'C\n", ""))


def get_RAM_info():
    mem_info = {}
    mem = psutil.virtual_memory()
    mem_info['mem_available'] = int(mem.available / 1024 / 1024)
    mem_info['mem_capacity'] = int(mem.total / 1024 / 1024)
    mem_info['mem_used'] = int(mem.used / 1024 / 1024)
    return mem_info


def get_CPU_usage():
    return psutil.cpu_percent()


def get_Disk_Space():
    hd = {}
    disk = os.statvfs("/")
    hd['disk_available'] = disk.f_bsize * disk.f_bavail
    hd['disk_capacity'] = disk.f_bsize * disk.f_blocks
    hd['disk_used'] = disk.f_bsize * disk.f_bfree
    return hd


def get_IP_addr():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('www.baidu.com', 0))
        ipAddress = s.getsockname()[0]
    except Exception as e:
        pass
    else:
        return ipAddress
    finally:
        s.close()

@logging_manager.logging_to_file
def gather_sys_info():
    sys_info = dict()
    mem_info = get_RAM_info()
    sys_info['timestamp'] = time.strftime('%X')
    sys_info['CPU_temp'] = get_CPU_temperature()
    sys_info['CPU_usage'] = get_CPU_usage()
    sys_info['RAM_used'] = mem_info['mem_used']
    sys_info['RAM_total'] = mem_info['mem_capacity']
    sys_info['ipAddress'] = get_IP_addr()
    return sys_info


def draw_image(size, sys_info):
    '''Draw image, size = (LCD.LCDWIDTH, LCD.LCDHEIGHT), sys_info '''
    # Load default font. or Alternatively load a TTF font.
    #font = ImageFont.load_default()
    font = ImageFont.truetype('visitor2.ttf', 12)

    # Create blank image for drawing.
    # Make sure to create image with mode '1' for 1-bit color.
    image = Image.new('1', size)

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)
    # Draw a white filled box to clear the image.
    draw.rectangle((0, 0, size), outline=255, fill=255)

    draw.text((2, 0), "{}".format(sys_info['timestamp']), font=font)
    draw.text((2, 10), "IP:{}".format(sys_info['ipAddress']), font=font)
    draw.text(
        (2, 20), "RAM:{}/{}MB".format(sys_info['RAM_used'], sys_info['RAM_total']), font=font)
    draw.text((2, 30), "CPU:{}%".format(sys_info['CPU_usage']), font=font)
    draw.text((2, 40), "CPU Temp:{}'C".format(sys_info['CPU_temp']), font=font)
    return image


def invert_color(image):
    image = image.convert('L')
    image = ImageOps.invert(image)
    image = image.convert('1')
    return image

if __name__ == '__main__':
    image = draw_image((LCDWIDTH, LCDHEIGHT), gather_sys_info())
    image.save('asd.bmp')
