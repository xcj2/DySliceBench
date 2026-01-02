import sys
sys.setrecursionlimit(100000)

def find(tab, a):
    if tab[0][a]==a:
        return a
    tab[0][a] = find(tab, tab[0][a])
    return tab[0][a]

def union(tab, a, b):
    p1, p2 = (find(tab, a), find(tab, b))
    if p1 != p2:
        tab[0][p1] = p2
        tab[1][p2] += tab[1][p1]

def size(tab, a):
    return tab[1][a]

N, M = [int(a) for a in input().split(" ")]
ABs = [[int(a) for a in input().split(" ")] for i in range(M)]
tab = [[i for i in range(N)], [1 for i in range(N)]]
arr = []

for a, b in reversed(ABs):
        a, b = (a-1, b-1)
        pa, pb = (find(tab, a), find(tab, b))
        na, nb = (size(tab, pa), size(tab, pb))
        if pa!=pb:
            dn = ((na+nb)*(na+nb-1)//2)-(na*(na-1)//2)-(nb*(nb-1)//2)
            arr.append(dn)
            union(tab, a, b)
        else:
            arr.append(0)

acc = 0
for cp in reversed(arr):
    acc += cp
    print(acc)
