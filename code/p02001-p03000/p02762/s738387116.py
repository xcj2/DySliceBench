from sys import stdin
from collections import defaultdict

N,M,K = [int(x) for x in stdin.readline().rstrip().split()]
F = []

par = [i for i in range(N+1)]
rank = [0] * (N+1)
size = [1] * (N+1)

def find(x):
    if par[x] == x:
        return par[x]
    else:
        par[x] = find(par[x])
        return par[x]
 
def union(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if rank[x] < rank[y]:
        par[x] = y
        size[y] += size[x]
        size[x] = 0
        
    else:
        par[y] = x
        size[x] += size[y]
        size[y] = 0
        if rank[x] == rank[y]:
            rank[x] += 1
 
def check_same(x,y):
    return find(x) == find(y)
 
def check_size(x):
    return size[find(x)]

friends = defaultdict(set)
for _ in range(M):
    A,B = [int(x) for x in stdin.readline().rstrip().split()]
    union(A,B)
    
    friends[A].add(B)
    friends[B].add(A)


block = defaultdict(set)
for _ in range(K):
    C,D = [int(x) for x in stdin.readline().rstrip().split()]
    block[C].add(D)
    block[D].add(C)

for i in range(1,N+1):
    ans = check_size(i)
    ans = ans - 1 - len(friends[i])
    for j in block[i]:
        if check_same(i,j):
          ans -= 1
    print(ans,end=" ")