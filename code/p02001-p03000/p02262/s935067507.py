import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
A = [0] * N
for i in range(N):
    a = I()
    A[i] = a
cnt = 0

def insertionSort(A, n, g):
    global cnt
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j = j - g
            cnt += 1
        A[j + g] = v

def shellSort(A, n):
    cnt = 0
    G = [1]
    j = 0
    while G[j] <= N:
        G.append(3 * G[j] + 1)
        j += 1
    m = len(G) - 1
    E = []
    for i in range(1, len(G)):
        E.append(G[len(G) - 1 - i])
    for i in range(len(G) - 1):
        insertionSort(A, n, E[i])
    print(m)
    print(' '.join(map(str, E)))


shellSort(A, N)

print(cnt)
for i in range(N):
    print(A[i])

