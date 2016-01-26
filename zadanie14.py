# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 15:34:32 2015

@author: student
"""
# zadanie 14: Napisz skrypt wyliczajacy wyznacznik macierzy wygenerowanej losowo

# import biblioteki Numpy
import numpy as np

# definicja macierzy 3x3 wygenerowanej losowo, zakres liczb 0 do 50
matrix = np.random.randint(50, size=(3, 3))
# definicja wyznacznika
wyznacznik = np.linalg.det(matrix)
# przedstawienie wynikow
print('Wygenerowana matryca 3x3:')
print(matrix)
print('Obliczony wyznacznik:')
print(wyznacznik)

