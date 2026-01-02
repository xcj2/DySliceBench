def rozwiaz(lista, k):
    wynik = [None] * len(lista)
    wynik[0] = 0
    for i in range(1, len(lista)):
        minimum = 1000000000000000
        for skok in range(1, k + 1):
            if skok <= i:
                proba = wynik[i - skok] + abs(lista[i] - lista[i - skok])
                if proba < minimum:
                    minimum = proba
        wynik[i] = minimum

    return wynik[len(lista) - 1]

def wczytaj_liste(): 
    wczytana_lista = input()
    lista_znakow = wczytana_lista.split()
    ostateczna_lista = []
    for element in lista_znakow:
        ostateczna_lista.append(int(element))
    return ostateczna_lista

def frog_2():
    N, K = wczytaj_liste()
    wysokosci = wczytaj_liste()
    print(rozwiaz(wysokosci, K))
    
frog_2()