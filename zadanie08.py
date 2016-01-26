# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 15:34:32 2015

@author: student
"""
# zadanie 8: Napisz skrypt sortujacy liczby malejaco. Wygeneruj losowo 50 liczb -
# wykorzystaj standardowa funkcje do losowania. Z wbudowanej funkcji
# sortujacej korzystaj tylko w celu werykacji wynikow

# import funkcji generujacej wartosci losowe ze standardowej biblioteki - random
from random import randint

# definicja funkcji sortujacej liczby malejaco
def sort(dane):
    
    for i in range(0,len(dane)):
        for j in range( 0, len(dane)-1):
            if dane[j] < dane[j+1]:
                temp = dane[j]
                dane[j] = dane[j+1]
                dane[j+1] = temp

# okreslenie ilosc liczb (50) oraz ich zakresu (od 0 do 100)
rawdata = dane = [randint(0,100) for x in range(0,50)]

# wyswietlenie wygenerowanych liczb
print('Dane wygenerowane')
print (dane) 
# sortowanie przy pomocy napisanego skryptu sort
sort(dane)
print('Dane posortowane za pomoca skryptu')
print (dane) 
# sprawdzenie wynikow z wykorzystaniem wbudowanej funkcji sortujacej (z parametrem odwrocenia wynikow)
print('Sprawdzenie sortowania')
rawdata.sort(reverse=True)
print (rawdata)