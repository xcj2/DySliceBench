import sys
sys.setrecursionlimit(10**9)

class Node:
    def __init__(self):
        self.p = -1
        self.l = -1
        self.r = -1

n = int(input())
T = [Node() for _ in range(n)]
D = [0]*n

def rec(u,p):
    D[u] = p
    if T[u].r != -1: rec(T[u].r,p)
    if T[u].l != -1: rec(T[u].l,p+1)

def printinfo(u):
    clst = []
    c = T[u].l
    while c != -1:
        clst.append(c)
        c = T[c].r
    if T[u].p == -1: ntype = "root"
    elif T[u].l == -1: ntype = "leaf"
    else: ntype = "internal node"
    print("node {}: parent = {}, depth = {}, {}, {}".format(u,T[u].p,D[u],ntype,clst))

for i in range(n):
    inp = [int(i) for i in input().split()]
    v = inp[0]
    d = inp[1]
    C = inp[2:]
    for j in range(d):
        c = C[j]
        if j == 0: T[v].l = c
        else: T[l].r = c
        l = c
        T[c].p = v
for i in range(n):
    if T[i].p == -1: r = i

rec(r,0)
for i in range(n): printinfo(i)
