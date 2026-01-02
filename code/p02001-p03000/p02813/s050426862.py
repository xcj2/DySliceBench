def wczytaj_liste(): 
    wczytana_lista = input()
    lista_znakow = wczytana_lista.split()
    ostateczna_lista = []
    for element in lista_znakow:
        ostateczna_lista.append(int(element))
    return ostateczna_lista 

def wartosc_bezwgledna(A): 
    if A >= 0: 
        return A
    else: 
        return -A 
    
def silnia(A): 
    if A == 0:
        return 0
    odp = 1
    for i in range(1, A+1):
        odp *= i
    return odp

from itertools import permutations 

def generuj_permutacje(N):
    lista = []
    if N == 0:
        return []
    if N == 1:
        return [1]
    else: 
        for i in range(1,N+1):
            lista.append(i)
    perm = permutations(lista)
    odp = []
    for i in list(perm): 
        odp.append(i)
    return odp  

def caunt_order(): 
    N = wczytaj_liste()[0]
    P = tuple(wczytaj_liste())
    Q = tuple(wczytaj_liste())
    permutacje = generuj_permutacje(N)
    for i in range(len(permutacje)):
        if P == permutacje[i]:
            nr_P = i
        if Q == permutacje[i]:
            nr_Q = i
    odp = nr_P - nr_Q
    print(wartosc_bezwgledna(odp))

caunt_order()