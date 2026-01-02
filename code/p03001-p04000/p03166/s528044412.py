def wczytaj_liste(): 
    wczytana_lista = input()
    lista_znakow = wczytana_lista.split()
    ostateczna_lista = []
    for element in lista_znakow:
        ostateczna_lista.append(int(element))
    return ostateczna_lista

def zrob_listy_sadziedztwa(lista): 
    listy_sasiedzitwa = {}
    for x, y in lista: 
        listy_sasiedzitwa[x] = []
        listy_sasiedzitwa[y] = []
    for x, y in lista: 
        listy_sasiedzitwa[y].append(x)
    return listy_sasiedzitwa

def wyjscie_do_szkoly_bfs(lista_zasad): 
    zasady = {}
    ile_niespelnionych = {}
    for rzecz1,rzecz2 in lista_zasad: 
        zasady[rzecz1] = [] 
        zasady[rzecz2] = []
        ile_niespelnionych[rzecz1] = 0 
        ile_niespelnionych[rzecz2] = 0
    for rzecz1, rzecz2 in lista_zasad: 
        zasady[rzecz1].append(rzecz2)
        ile_niespelnionych[rzecz2] += 1
    kolejnosc_ubioru = [rzecz for rzecz in zasady if ile_niespelnionych[rzecz] == 0]
    nr_przegladnanego = 0
    while nr_przegladnanego < len(kolejnosc_ubioru): 
        for ubranie in zasady[kolejnosc_ubioru[nr_przegladnanego]]: 
            ile_niespelnionych[ubranie] -= 1
            if ile_niespelnionych [ubranie] == 0:
                kolejnosc_ubioru.append(ubranie)
        nr_przegladnanego += 1
    if len(kolejnosc_ubioru) != len(zasady): 
        raise Exception('Nie można się ubrać Skurwysynu')
    return kolejnosc_ubioru 

def longest_patch(): 
    N, M = wczytaj_liste()
    lista_krawedzi = []
    for i in range(M): 
        x, y = wczytaj_liste()
        lista_krawedzi.append((x,y))
    listy_krawedzi = zrob_listy_sadziedztwa(lista_krawedzi)
    kolejnosc = wyjscie_do_szkoly_bfs(lista_krawedzi)
    najdluzsze_drogi = {}
    for wierzcholek in kolejnosc: 
        if len(listy_krawedzi[wierzcholek]) == 0: 
            najdluzsze_drogi[wierzcholek] = 0
        else: 
            maksimum = 0 
            for x in listy_krawedzi[wierzcholek]: 
                if najdluzsze_drogi[x]> maksimum:
                      maksimum = najdluzsze_drogi[x]
            najdluzsze_drogi[wierzcholek] = maksimum + 1
    najdluzsza = 0 
    for a_chuj_wie_co in najdluzsze_drogi: 
        if najdluzsze_drogi[a_chuj_wie_co] > najdluzsza:
            najdluzsza = najdluzsze_drogi[a_chuj_wie_co]
    print (najdluzsza)

longest_patch()  