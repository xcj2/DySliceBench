def wczytaj_liste(): 
    wczytana_lista = input()
    lista_znakow = wczytana_lista.split()
    ostateczna_lista = []
    for element in lista_znakow:
        ostateczna_lista.append(int(element))
    return ostateczna_lista

def rozwiaz(lista):
    if len(lista)==1:
        return 0
    if len(lista)==2:
        return abs(lista[0]-lista[-1])
    wynik_1 = abs(lista[0]-lista[1])+rozwiaz(lista[1:])
    wynik_2 = abs(lista[0]-lista[2])+rozwiaz(lista[2:])
    if wynik_1 < wynik_2:
        return wynik_1
    else:
        return wynik_2

def rozwiaz(lista):
    prawy, lewy = 0, abs(lista[-1] - lista[-2])
    while len(lista) > 2:
        prawy, lewy = lewy, min(prawy + abs(lista[-1] - lista[-3]),
                                lewy + abs(lista[-2] - lista[-3]))
        lista.pop()
    return lewy
    
def frog_1():
    N = wczytaj_liste()[0]
    wysokosci = wczytaj_liste()
    wynik = rozwiaz(wysokosci)
    print(wynik)
    
    
frog_1()