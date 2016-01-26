# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 15:08:21 2015

@author: student
"""
# zadanie 7: Napisz skrypt obliczajacy pierwiastki równania kwadratowego w postaci:
# y = ax2 + bx + c. Wejsciem skryptu sa wartosci: a, b, c

# import funkcji obliczajacej pierwiastek kwadratowy (sqrt) ze standardowej biblioteki - math
from math import sqrt
 
# wprowadzenia wartosci a, b oraz c
print('Skrypt rozwiazuje rownanie typu kwadratowe typu y=ax^2+bx+c')
a = int(input("Podaj wartosc a: "))
b = int(input("Podaj wartosc b: "))
c = int(input("Podaj wartosc c: "))

#deficinja Delty
delta = (b**2)-(4*a*c)

# obliczenie pierwiastkow w zaleznosci od wartosci Delty
wynik = ((delta < 0) and "Brak pierwiastków") or \
((delta == 0) and ("x = {}".format(-b / (2 * a)))) or \
((delta > 0) and ("x1 = {}, x2 = {}".format((-b - sqrt(delta)) / (2 * a), (-b + sqrt(delta)) / (2 * a))))

# wyswietlenie wynikow
print (wynik)