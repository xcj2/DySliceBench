def wczytaj_liste(): 
    wczytana_lista = input()
    lista_znakow = wczytana_lista.split()
    ostateczna_lista = []
    for element in lista_znakow:
        ostateczna_lista.append(int(element))
    return ostateczna_lista 

def BFS(dziecko, listy_znajomosci): 
    do_przejrzenia = [dziecko]
    odleglosc = {dziecko:0}
    nr_przegladanego = 0 
    while nr_przegladanego < len(do_przejrzenia): 
        aktualnie_przegladany = do_przejrzenia[nr_przegladanego]
        for kumpel in listy_znajomosci[aktualnie_przegladany]: 
            if kumpel not in odleglosc: 
                do_przejrzenia.append(kumpel)
                odleglosc[kumpel] = odleglosc[aktualnie_przegladany] + 1 
        nr_przegladanego +=1
    return max(odleglosc.values())

def labirynt(): 
    H, W = wczytaj_liste()
    labirynt = []
    for i in range(H): 
        rzadek = [x for x in (input() + '#')]
        labirynt.append(rzadek)
    labirynt.append(['#']*W)
    lista_krawedzi = []
    for i in range(H):
        for j in range(W):
            if labirynt[i][j] == '.':
                if labirynt[i+1][j] == '.':
                    lista_krawedzi.append(((i,j),(i+1,j)))
                if labirynt[i][j+1] == '.':
                    lista_krawedzi.append(((i,j),(i,j+1)))
    listy_krawedzi = {}
    for x, y in lista_krawedzi:
        listy_krawedzi[x] = []
        listy_krawedzi[y] = []
    for x, y in lista_krawedzi:  
        listy_krawedzi[x].append(y)
        listy_krawedzi[y].append(x)
    maksymalny = 0
    for i in range(H):
        for j in range(W):
            if labirynt[i][j] == '.':
                kandydat = BFS((i,j),listy_krawedzi)
                if kandydat > maksymalny: 
                    maksymalny = kandydat
    print(maksymalny)

labirynt()