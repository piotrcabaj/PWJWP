# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 14:10:00 2015

@author: student
"""
# zadanie 3: Napisz skrypt zliczajacy ilosc plikow w katalogu /dev, skorzystaj ze standardowej
# biblioteki - os

# zaimportowanie standardowej biblioteki - os
import os, os.path

# okreslenie katalogu dla, ktorego program ma zliczac ilosc plikow
DIR = '/dev'
# wyswietlenie ilosci katalogow przy pomocy polecenia z bilbioteki - os
print(len([name for name in os.listdir(DIR)]))