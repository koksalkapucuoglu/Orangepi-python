import os
import sys

temp = open ("/sys/devices/virtual/thermal/thermal_zone0/temp")
thetext=temp.read()
temp.close()
temp = thetext.split("\n")[1].split(" ")[9]
temperature = float(tempdata[2:])
temperature = str(temperature / 1000)
print temperature

