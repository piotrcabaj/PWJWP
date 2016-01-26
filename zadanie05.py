# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 14:20:07 2015

@author: student
"""
# zadanie 5: Napisz rekurencyjne przejscie drzewa katalogow i wypisanie plikow, ktore
# znajduja sie w eksplorowanej strukturze

# zaimportowanie standardowej biblioteki - os
import os, os.path

# definicja funkcji rekurencyjnej cnt
def cnt(list_dirs, dir_src):
    print(list_dirs)
    for item in list_dirs:
        wh = dir_src+'/'+item
        if os.path.isdir(wh):
            cnt(os.listdir(wh), wh)
            
    return
# określenie katalogu oraz wypisanie nazw plikow
DIR = "/home/student/Documents/"
list_dirs = os.listdir(DIR)
cnt(list_dirs, DIR)