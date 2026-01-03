from collections import defaultdict
def root(x, par):
    while par[x] >= 0:
        x = par[x]
    return x

def unite(x,y,par):
    rx = root(x,par)
    ry = root(y,par)
    if rx != ry:
        if rx > ry:
            rx, ry = ry, rx
        par[rx] += par[ry]
        par[ry] = rx

def same(x,y,par):
    rx = root(x,par)
    ry = root(y,par)
    return rx == ry

def size(x, par):
    return -par[root(x,par)]

N, K, L = map(int, input().split())
par1 = [-1]*N
par2 = [-1]*N

for i in range(K):
    A, B = map(int, input().split())
    A, B = A-1, B-1
    unite(A, B, par1)

for i in range(L):
    C, D = map(int, input().split())
    C, D = C-1, D-1
    unite(C, D, par2)

G = defaultdict(list)
for i in range(N):
    G[(root(i, par1), root(i, par2))].append(i)
Ans = [0]*N
for city_list in G.values():
    for city in city_list:
        Ans[city] = len(city_list)
for i in Ans:
    print(i, end=" ")