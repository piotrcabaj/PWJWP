# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 14:27:57 2016

@author: student
"""

# Python 2 - zadanie 2: zdeniowac klase reprezentujaca liczby zespolone (wraz z funkcjami na
# nich dzialajacymi np. modul dodawanie, odejmowanie itd.),

# definicja klasy wraz funkcjami dodawania (add), odejmowania (sub) oraz mnozenia (mul)
# liczb zespolonych
class lz:
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def add(self, other):
        return lz(self.real + other.real,
                  self.imag + other.imag)

    def sub(self, other):
        return lz(self.real - other.real,
                  self.imag - other.imag)

    def mul(self, other):
        return lz(self.real*other.real - self.imag*other.imag,
                  self.imag*other.real + self.real*other.imag)

# definicja liczb zespolonych
l1 = lz(2,1)
l2 = lz(3,3)

# operacje z wykorzystaniem zdefiniowanej klasy
dod = lz.add(l1, l2)
ode = lz.sub(l1, l2)
mno = lz.mul(l1, l2)

# przedstawienie wynikow
print ("Dodawanie dwoch liczb zespolonych (2 + i)+(3 +3i):")
print (dod.real,"+",dod.imag,"i")
print ("Odejmowanie dwoch liczb zespolonych (2 + i)-(3 +3i):")
print (ode.real,"+",ode.imag,"i")
print ("Mnozenie dwoch liczb zespolonych (2 + i)*(3 +3i):")
print (mno.real,"+",mno.imag,"i")