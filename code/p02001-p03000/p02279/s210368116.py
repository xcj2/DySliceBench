import sys
input = sys.stdin.readline
sys.setrecursionlimit(2**20)

class Node():
    def __init__(self):
        self.p = None
        self.l_ch = None
        self.r_si = None

def SetDepth(u, p):
    D[u] = p
    if T[u].r_si != None:
        SetDepth(T[u].r_si, p)
    if T[u].l_ch != None:
        SetDepth(T[u].l_ch, p+1)

def SetAttribute():
    for i in range(n):
        if T[i].p == -1:
            A[i] = 'root'
        elif T[i].l_ch == None:
            A[i] = 'leaf'
        else:
            A[i] = 'internal node'

n = int(input())
T = [None] * n
for i in range(n):
    temp = Node()
    T[i] = temp
C = [[] for i in range(n)]

for i in range(n):
    L = [int(x) for x in input().split()]
    v, d = L[0], L[1]
    C[v] = L[2:]
    for j, c in enumerate(L[2:]):
        if j == 0:
            T[v].l_ch = c
        else:
            T[l].r_si = c
        l = c
        T[c].p = v

D = [0] * n
for i in range(n):
    if T[i].p == None:
        T[i].p = -1
        r = i
SetDepth(r, 0)

A = [''] * n
SetAttribute()

for i in range(n):
    print('node {}: parent = {}, depth = {}, {}, {}'.format(i, T[i].p, D[i], A[i], C[i]))
