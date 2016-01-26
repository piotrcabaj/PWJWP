# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 15:34:32 2015

@author: student
"""
#zadanie 13: Napisz skrypt realizujacy mnozenie dwoch macierzy o rozmiarach 8x8

# import biblioteki Numpy
import numpy as np

# definicja macierzy 8x8, wygenerowane losowo, zakres liczb 0 do 20
matrix1 = np.random.randint(20, size=(8, 8))
matrix2 = np.random.randint(20, size=(8, 8))
# mnozenie macierzy
multiply = matrix1 * matrix2

# przedstawienie wynikow
print('Macierz 8x8 nr 1:')
print(matrix1)
print('Macierz 8x8 nr 2:')
print(matrix2)
print('Wynik mnozenia macierzy 1 i 2:')
print(multiply)
