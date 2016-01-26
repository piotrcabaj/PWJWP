# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 14:13:09 2015

@author: student
"""
#zadanie 4: Napisz skrypt realizujacy funkcje zamka szyfrowego. Prosi o podanie kodu
# i nastepnie sprawdza czy jest on zgodny z wczesniej wprowadzonym kodem

# kod
p = "piotrek"
# zapytanie o kod
key = input("Podaj kod: \n")

# sprawdzenie, czy kod jest poprawny i w zaleznosci od wyniku wygenerowanie odpowiedniego komunikatu
if key == p:
    print ( "OK\n" )
else:
    print( "Niestety, kod nie jest OK\n" )