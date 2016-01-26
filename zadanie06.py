# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 15:28:15 2015

@author: student
"""
# zadanie 6: Napisz skrypt konwersji rozszerzen plików *.jpg na *.png (uprzednio stworz
# zestaw 4 plików z rozszerzeniem *.jpg)

# import standardowej biblioteki - os
import os, os.path
from os import listdir
from os.path import isfile, join

# okreslenie katalogu, w ktorym ma sie odbyc konwersja
DIR = "/home/student/Documents/Piotrek/zadanie6_files/"

# skrypt zamieniajacy 4 pliki z rozszerzeniem .jpg na 4 pliki z rozszerzeniem .png
onlyfiles = [f for f in listdir(DIR) if isfile(join(DIR,f))]

for item in onlyfiles:
    if item.find(".jpg") > 0:
        os.rename( DIR+item, DIR+item[:-4]+".png")