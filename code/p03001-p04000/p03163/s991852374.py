def wczytaj_liste(): 
    wczytana_lista = input()
    lista_znakow = wczytana_lista.split()
    ostateczna_lista = []
    for element in lista_znakow:
        ostateczna_lista.append(int(element))
    return ostateczna_lista

def plecak_rozwiazanie(pojemnosc, lista_przedmiotow): 
    bez_przedmiotu = [0] * (pojemnosc + 1)
    for waga, wartosc in lista_przedmiotow:
        z_przedmiotem = [None] * (pojemnosc + 1)
        for i in range(pojemnosc+1): 
            if waga > i: 
                z_przedmiotem[i] = bez_przedmiotu[i]
            else: 
                z_przedmiotem[i] = max(bez_przedmiotu[i-waga]+wartosc, bez_przedmiotu[i])
        bez_przedmiotu = z_przedmiotem
    return bez_przedmiotu[pojemnosc]

def plecak_1(): 
    N, W = wczytaj_liste()
    przedmioty = []
    for i in range(N): 
        waga, wartosc = wczytaj_liste()
        przedmioty.append((waga, wartosc))
    print (plecak_rozwiazanie(W,przedmioty))   
    
plecak_1()