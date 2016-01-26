"""
Created on Sat Dec 19 15:34:32 2015

@author: student
"""
# zadanie 9: Napisz skrypt usuwajacy z wejsciowego ciagu tekstowego (wybierz kilka
# plików z repozytorium: Tekstowego) nastapujace slowa : sie, i, oraz, nigdy, dlaczego

# wybor pliku z repozytorium, tylko plik Polsat.txt zawieral polskie slowa, reszta jest w j. angielskim
filename="Polsat.txt"
# otwarcie pliku tekstowego, wczytanie tekstu do 'g' oraz zamkniecie pliku
with open(filename,'r') as f:
    g=f.read()
f.close()

# wyswietlenie zawartosci pliku przed zmianami
print('===== Listing pliku Polsat.txt przed zmianami: \n')
print(g)

# usuniecie zdefiniowanych slow, slowa 'sie' oraz 'i' wraz ze spacjami aby usunac tylko spojniki
g = g.replace(" sie ","  ")
g = g.replace(" i ","  ")
g = g.replace("oraz","")
g = g.replace("nigdy","")
g = g.replace("Dlaczego","")

# wyswietlenie pliku po zmianach
print('\n===== Listing pliku Polsat.txt po zmianach: \n')
print(g)
