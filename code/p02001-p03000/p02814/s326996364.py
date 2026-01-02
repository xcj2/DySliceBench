def wczytaj_liste(): 
    wczytana_lista = input()
    lista_znakow = wczytana_lista.split()
    ostateczna_lista = []
    for element in lista_znakow:
        ostateczna_lista.append(int(element))
    return ostateczna_lista 

def NWD(A,B): 
    if B == 0: 
        return A
    else: 
        return NWD(B, A%B)  

def nww(x, y): 
    return x*y // NWD(x,y)

def pol_wielokrotnosci(): 
    N, M = wczytaj_liste()
    A = wczytaj_liste()
    potega_2 = A[0]&-A[0]
    for liczba in A:
        if liczba&-liczba != potega_2:
            print(0)
            return
    najmiejsza_wspolna_listy = A[0]
    for i in range(1,len(A)):
        najmiejsza_wspolna_listy = nww(najmiejsza_wspolna_listy, A[i])
        if najmiejsza_wspolna_listy//2 > M:
            print(0)
            return     
    odp = (M - najmiejsza_wspolna_listy//2) // najmiejsza_wspolna_listy + 1
    print(odp)

pol_wielokrotnosci()