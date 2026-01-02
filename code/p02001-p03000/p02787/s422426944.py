def wczytaj_liste():
    ciag = input()
    rozdzielona_lista = ciag.split()
    odp = []
    for wyraz in rozdzielona_lista:
        liczba = int(wyraz)
        odp.append(liczba)
    return odp

def rzucanie_zaklenc(zycie, lista_zaklenc):
    koszt_zaklenc = [10**9] * (zycie+1)
    koszt_zaklenc[0] = 0
    for damage, cost in lista_zaklenc:
        for i in range(zycie+1):
            if i - damage >= 0:
                if cost+koszt_zaklenc[i-damage]< koszt_zaklenc[i]:
                    koszt_zaklenc[i] = cost+koszt_zaklenc[i-damage]
            else:
                if cost < koszt_zaklenc[i]:
                    koszt_zaklenc[i] = cost
    return koszt_zaklenc[zycie]

def E():
    H, N = wczytaj_liste()
    zaklencia = []
    for i in range(N):
        damage, cost = wczytaj_liste()
        zaklencia.append((damage, cost))
    print(rzucanie_zaklenc(H, zaklencia))

E()

