# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 15:51:27 2015

@author: student
"""
# zadanie 11: Napisz skrypt obliczajacy wartosc iloczynu dwoch wektorow : a = [1, 2, 12, 4],
# b = [2, 4, 2, 8], tzw. iloczyn skalarny wektorów

# definicja wektorow a oraz b
a = [1, 2, 12, 4]
b = [2, 4, 2, 8]

# definicja iloczynu skalarnego wektorow
def iloczyn(u,v):
    return sum([a * b for a,b in zip(u,v)])

# wyswietlenie wynikow
print('Iloczyn skalarny wektorow a=[1,2,12,4] oraz b=[2,4,2,8] wynosi:',iloczyn(a,b))
