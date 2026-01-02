def wczytaj_liste(): 
    wczytana_lista = input()
    lista_znakow = wczytana_lista.split()
    ostateczna_lista = []
    for element in lista_znakow:
        ostateczna_lista.append(int(element))
    return ostateczna_lista

def plecak_rozwiazanie_2(pojemnosc, lista_przedmitow):
    bez_przedmiotu = [0] + [10**18] * len(lista_przedmitow) * 1000
    for waga, wartosc in lista_przedmitow:
        z_przedmiotem = [None] * (len(lista_przedmitow) * 1000 +1)
        for i in range(len(z_przedmiotem)): 
            if wartosc > i: 
                z_przedmiotem[i] = bez_przedmiotu[i]
            else: 
                z_przedmiotem[i] = min(bez_przedmiotu[i-wartosc]+waga, bez_przedmiotu[i])
        bez_przedmiotu = z_przedmiotem
    for i in reversed(range(len(bez_przedmiotu))):
        if bez_przedmiotu[i] <= pojemnosc:
            return i

def plecak_2():
    N, W = wczytaj_liste()
    przedmioty = []
    for i in range(N): 
        waga, wartosc = wczytaj_liste()
        przedmioty.append((waga, wartosc))
    print (plecak_rozwiazanie_2(W,przedmioty))  
    
plecak_2()