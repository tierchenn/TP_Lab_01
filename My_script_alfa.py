import platform
import sys
import os
import socket
import shutil
import locale
import time
import json
data = []; keys = []
keys += ["user", "current working directory"]; data += [os.getlogin(),   os.getcwd()] #why print unicod? answer: encoding="utf-8"
systema = str(platform.system())
# OC, node, release, version, machine
keys += ["OC, node, release, version, machine"]; data += [platform.uname()] #change for easest analog
# processor, architecture
keys += ["processor", "architecture"]; data += [platform.processor(),   platform.architecture()]
# Pyton version
keys += ["Pyton version"]; data += [sys.version]
# number of logical CPU cores
keys += ["number of logical CPU cores"]; data += [os.cpu_count()]
# IP
keys += ["IP"]; data += [socket.gethostbyname(socket.gethostname())]
#disk_usage 
keys += ["disk_usage"]; data += [shutil.disk_usage('/')]
#regional settings 
keys += ["regional"]; data += [locale.getdefaultlocale()]
#Time (!)
keys += ["time_format"]; data += [time.tzname]
if systema == "Windows":
    keys += ["system", "edition", "Iot", "platform"]; data += [systema, platform.win32_edition(), platform.win32_is_iot(), platform.win32_ver()]
elif systema == "Linux":
    keys += ["system", "OS", "name"]; data += [systema, platform.freedesktop_os_release(), os.uname()]
    # CPU model
    with open('/proc/cpuinfo') as f:
        for line in f:
            if 'model name' in line:
                keys += ["CPU model"]; data += [line.strip()]
                break
    # Temperature
    with open('/sys/class/thermal/thermal_zone0/temp') as f:
        keys += ["Temperature"]; data += [int(f.read()) / 1000, 'C']
    # Uptime
    with open('/proc/uptime') as f:
        keys += ["uptime"]; data += [f.read()]
    # Memory
    with open('/proc/meminfo') as f:
        keys += ["Memory"]; data += [f.read()]

user_dict = dict(zip(keys, data))

s = 0; res = []
for rabot in user_dict["disk_usage"]:
    rabot  = int(rabot)
    alf = ['B', 'KB', 'MB', 'GB', 'TB']; status = ["Curent", "Usage", "Free"]
    n = 0; 
    while rabot >= 1024:
        rabot = rabot/1024
        n += 1
    res += [status[s] + " " + str(rabot) + " " + alf[n]]
    s+=1
user_dict["disk_usage"] = res

s = 0; res = []
for rabot in user_dict["regional"]:
    alf = ['LC_CTYPE:', 'LANG:']
    res += [alf[s] + " " + str(rabot)]
    s += 1
user_dict["regional"] = res
with open("result.json", "w", encoding="utf-8") as file:
    json.dump(user_dict, file, ensure_ascii=False, indent = 2)
    print("Programm complete")
