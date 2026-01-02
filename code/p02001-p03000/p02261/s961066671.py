def sep(Nf, Mf):
    mm = [[] for _ in range(9)]
    for m in range(len(Nf)):
        for i in range(9):
            if Nf[m] == i+1:
                mm[i].append(Mf[m])
    return mm


def ssort(L, N, M):
    for i in range(len(N)-1):
        x = N[i+1:].index(min(N[i+1:])) + i + 1
        if N[i] > N[x]:
            L[i], L[x] = L[x], L[i]
            N[i], N[x] = N[x], N[i]
            M[i], M[x] = M[x], M[i]


def bsort(L, N, M):
    for i in range(len(N)-1):
        for j in range(len(N)-1-i):
            if N[j] > N[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
                N[j], N[j+1] = N[j+1], N[j]
                M[j], M[j+1] = M[j+1], M[j]


n = int(input())
L = list(input().split())
N = [int(i[1]) for i in L]
M = [i[0] for i in L]
marks = ['S', 'H', 'C' ,'D']
Lb, Nb, Mb = L[:], N[:], M[:]
bsort(Lb, Nb, Mb)
print(' '.join(Lb))
if sep(N, M) == sep(Nb, Mb):
    print('Stable')
else:
    print('Not stable')

Ls, Ns, Ms = L[:], N[:], M[:]
ssort(Ls, Ns, Ms)
print(' '.join(Ls))
if sep(N, M) == sep(Ns, Ms):
    print('Stable')
else:
    print('Not stable')
