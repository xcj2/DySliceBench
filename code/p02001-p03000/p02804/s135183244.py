def wczytaj_liste(): 
    wczytana_lista = input()
    lista_znakow = wczytana_lista.split()
    ostateczna_lista = []
    for element in lista_znakow:
        ostateczna_lista.append(int(element))
    return ostateczna_lista 


class N_po_K:
    def __init__(self, maxN, modulo = 10**9+7): 
        self.modulo = modulo
        self.silnie = [1]
        for i in range(1, maxN + 1):
            self.silnie.append(self.silnie[i - 1] * i % self.modulo)
        
    def dwumian(self, N, K):
        if N < K: 
            return 0
        return self.silnie[N] * pow(self.silnie[K], self.modulo - 2, self.modulo)\
                              * pow(self.silnie[N-K], self.modulo - 2, self.modulo) % self.modulo

def min_max_sums(): 
    N, K = wczytaj_liste()
    A = wczytaj_liste()
    A.sort()
    suma_min = 0 
    suma_max = 0
    dwumianator = N_po_K(N)
    for i in range(N):
        suma_min += dwumianator.dwumian(N-i-1, K-1)*A[i]
        suma_max += dwumianator.dwumian(N-i-1, K-1)*A[-i-1]
    print((suma_max - suma_min)%(10**9+7))

min_max_sums()