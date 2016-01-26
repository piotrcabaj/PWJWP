# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 15:34:32 2015

@author: student
"""
# zadanie 10: Napisz skrypt zmieniajacy w podanym ciagu wej±ciowym (wybierz kilka
# plików z repozytorium: Tekstowego) nastepujace slowa : i, oraz, nigdy, dlaczego
# na nastepujacy zestaw slów : oraz, i, prawie nigdy, czemu. Zalecana struktura jest slownik.

# otwarcie pliku tekstowego, wczytanie tekstu do 'g' oraz zamkniecie pliku
filename="Polsat.txt"
with open(filename,'r') as f:
    g=f.read()
f.close()

# wyswietlenie zawartosci pliku przed zmianami
print('===== Listing pliku Polsat.txt przed zmianami: \n')
print(g)

# definicja slownika, aby zapobiec podwojnej zamianie 'i' na 'oraz' a potem znow na 'i'
# zamieniono 'i' na 'orazX', ktory w dalszym kroku zamieniono ostatecznie na 'oraz'
# podobnie z wyrazeniem 'prawie nigdy' zamieniono na 'prawienigdy'
# podmiana z 'nigdy' na 'prawie nigdy' nastepuje w nastepnym kroku
slownik1 = {' i ':' orazX ',' oraz ':' i ','prawie nigdy':'prawienigdy',\
           'Dlaczego':'czemu','Polsat':'TVN'}

# podmiane slow na podstawie zdefiniowanego slownika
for key in slownik1:
    g = g.replace(key, slownik1[key])
# podmiana sztucznie stworzonych w slowniku zamian na te okreslone w zadaniu
slownik2 = {' orazX ':' oraz ',' nigdy ':' prawie nigdy ','prawienigdy':'prawie nigdy'}
for key in slownik2:
    g = g.replace(key, slownik2[key])
print('\n===== Listing pliku Polsat.txt po zmianach: \n')
print(g)
