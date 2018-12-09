#!/bin/bash
cd /home/pi/run/sys_status
/home/pi/projects/PCD_8544_screen/cpu_show/BL/backlight_ctrl ON
nohup python3 sys_status.py &
