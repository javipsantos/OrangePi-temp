#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
# author    : "javier pérez santos para orangepiweb.es"
# credits   : "javier pérez santos, orangepiweb.es"
# copyright : "Copyright 2018, orangepiweb.es"
#
#   ___                             ____  ___        __   _
#  / _ \ _ __ __ _ _ __   __ _  ___|  _ \(_) \      / /__| |__   ___  ___
# | | | | '__/ _` | '_ \ / _` |/ _ \ |_) | |\ \ /\ / / _ \ '_ \ / _ \/ __|
# | |_| | | | (_| | | | | (_| |  __/  __/| | \ V  V /  __/ |_) |  __/\__ \
#  \___/|_|  \__,_|_| |_|\__, |\___|_|   |_|  \_/\_/ \___|_.__(_)___||___/
#                        |___/
#
# Control de temperatura del micro

import os
import sys
import subprocess
from time import sleep

from pyA20.gpio import gpio
from pyA20.gpio import port

ventilador = port.PA6
gpio.init()

gpio.setcfg(ventilador, gpio.OUTPUT)
temperaturamaxima = 45

while True:
        temp = int(os.popen('cat /sys/class/thermal/thermal_zone0/temp').read())
        #como se presenta la temperatura en milésimas de grado, dividimos por 1000
        temp = temp / 1000
        if temp >= temperaturamaxima:
                gpio.output(ventilador,1)
        else:
                gpio.output(ventilador,0)
        sleep (60)