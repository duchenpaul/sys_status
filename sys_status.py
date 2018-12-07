import time
import PIL.ImageOps

import image_generate
import show_in_LCD
import read_config

config_file = 'screen_config.ini'

config = read_config.read_config_general(configFile=config_file)

LCDWIDTH, LCDHEIGHT = int(config['SCREEN']['LCDWIDTH']), int(config['SCREEN']['LCDHEIGHT'])

disp = show_in_LCD.PCD8544_Display(**show_in_LCD.get_config(config_file))

while True:
    t1 = time.time()
    image = image_generate.draw_image((LCDWIDTH, LCDHEIGHT), image_generate.gather_sys_info())
    disp.display_image(image_generate.invert_color(image))
    t2 = time.time()
    # Remove the running time to make sure it takes exactly 1 sec every time 
    sleeptime = (1 - (t2 - t1)) if (1 - (t2 - t1)) > 0 else 0
    time.sleep(sleeptime)