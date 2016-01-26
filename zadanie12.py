# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 15:34:32 2015

@author: student
"""
# zadanie 12: Napisz skrypt sumujacy dwie macierze o rozmiarach 128x128. Wykorzystaj
# generator liczb losowych do wygenerowania macierzy. Zrealizuj operacje
# z wykorzystaniem Numpy

# import biblioteki Numpy
import numpy as np

# definicja macierzy losowych - rozmiar 128x128, zakres liczb od 0 do 100
matrix1 = np.random.randint(100, size=(128, 128))
matrix2 = np.random.randint(100, size=(128, 128))
suma = matrix1 + matrix2

# przedstawienie wynikow
print('Matryca nr 1:')
print(matrix1)
print('Matryca nr 2:')
print(matrix2)
print('Suma obydwu matryc:')
print(suma)


