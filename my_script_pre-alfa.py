import platform
import sys
import os
import socket
import shutil
import locale
import time

print("current working directory & user:", os.getlogin(), os.getcwd())
systema = str(platform.system())
# OC, node, release, version, machine
print(platform.uname())
# processor, architecture
print(platform.processor(), platform.architecture())
print("Pyton version:", sys.version)
print("number of logical CPU cores:", os.cpu_count())
# terminal size
print(os.get_terminal_size())
print("IP:", socket.gethostbyname(socket.gethostname()))
print("disk_usage:",shutil.disk_usage('/'))
print("regional settings:", locale.getdefaultlocale())
print("Time:", time.tzname)
if systema == "Windows":
    print(systema, platform.win32_edition(), "IoT:", platform.win32_is_iot(), platform.win32_ver())
elif systema == "Linux":
    print(systema, platform.freedesktop_os_release(), os.uname())
    # CPU model
    with open('/proc/cpuinfo') as f:
        for line in f:
            if 'model name' in line:
                print(line.strip())
                break
    # Temperature
    with open('/sys/class/thermal/thermal_zone0/temp') as f:
        print(int(f.read()) / 1000, 'C')
    # Uptime
    with open('/proc/uptime') as f:
        print(f.read())
    # Memory
    with open('/proc/meminfo') as f:
        print(f.read())
