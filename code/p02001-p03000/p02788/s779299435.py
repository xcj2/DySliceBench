def wczytaj_liste():
    ciag = input()
    rozdzielona_lista = ciag.split()
    odp = []
    for wyraz in rozdzielona_lista:
        liczba = int(wyraz)
        odp.append(liczba)
    return odp

def F_symulacja():
    N, D, A = wczytaj_liste()
    monstery = []
    for i in range(N):
        x, h = wczytaj_liste()
        monstery.append((x, h))
    monstery.sort()
    wynik = 0
    while len(monstery) > 0:
        x, h = monstery[0]
        if h <= 0:
            monstery.pop(0)
            continue
        bomba_x = x + D
        wynik += 1
        for i in range(len(monstery)):
            x_i, h_i = monstery[i]
            if bomba_x - D <= x_i <= bomba_x + D:
                monstery[i] = (x_i, h_i - A)

    print(wynik)

def zabij(H, A):
    if H % A == 0:
        return H // A
    else:
        return H // A + 1

def F():
    N, D, A = wczytaj_liste()
    monstery = []
    for i in range(N):
        x, h = wczytaj_liste()
        monstery.append((x, h))
    monstery.sort()

    wynik = 0
    gdzie_sie_koncza_bomby = []
    skonczone = 0
    ile_tu_spadlo = 0
    for x, h in monstery:
        while len(gdzie_sie_koncza_bomby) > skonczone:
            bomby_do, ile_bomb = gdzie_sie_koncza_bomby[skonczone]
            if bomby_do < x:
                ile_tu_spadlo -= ile_bomb
                skonczone += 1
            else:
                break
        if h - ile_tu_spadlo * A > 0:
            zrzucam_tutaj = zabij(h - ile_tu_spadlo * A, A)
            wynik += zrzucam_tutaj
            ile_tu_spadlo += zrzucam_tutaj
            gdzie_sie_koncza_bomby.append((x + 2 * D, zrzucam_tutaj))
    print(wynik)

F()