def wczytaj_liste(): 
    wczytana_lista = input()
    lista_znakow = wczytana_lista.split()
    ostateczna_lista = []
    for element in lista_znakow:
        ostateczna_lista.append(int(element))
    return ostateczna_lista

def wszystkie_mozliwosci(N):
    if N==0:
        return [[]]
    poprzedni = wszystkie_mozliwosci(N-1)
    wynik = []
    for przyp in poprzedni:
        wynik.append(przyp + [False])
        wynik.append(przyp + [True])
    return wynik

def C():
    N = wczytaj_liste()[0]
    zeznania = []
    odp = 0
    for i in range(N):
        A = wczytaj_liste()[0]
        zeznania.append([])
        for j in range(A):
            x, y = wczytaj_liste()
            zeznania[-1].append((x-1,y))
    
    for czy_szczery in wszystkie_mozliwosci(N):
        dasie = True
        for i in range(N):
            if czy_szczery[i]:
                for x,y in zeznania[i]: 
                    if y == 1 and not czy_szczery[x]:
                        dasie = False
                    if y == 0 and czy_szczery[x]:
                        dasie = False
        if dasie:
            ile_szczerych = sum(czy_szczery)
            if ile_szczerych > odp:
                odp = ile_szczerych

    print(odp)
C()