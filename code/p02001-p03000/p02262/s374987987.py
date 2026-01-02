from sys import stdin
from copy import deepcopy
input = stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]

B = deepcopy(A)
S = deepcopy(A)


def p(N):
    for i in range(len(N)):
        if i == len(N) - 1:
            print(N[i])
        else:
            print(N[i], end=" ")


cnt = 0


def insertionsort(n, g):
    global cnt
    for i in range(g, N):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j = j - g
            cnt += 1
        A[j + g] = v


def shellsort(n):
    h = 1
    G = []

    while h <= n:
        G.append(h)
        h = 3 * h + 1

    G.reverse()
    m = len(G)

    print(m)
    p(G)

    for i in range(0, m):
        insertionsort(n, G[i])


shellsort(N)

print(cnt)

for a in A:
    print(a)

