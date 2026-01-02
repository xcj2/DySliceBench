import sys
sys.setrecursionlimit(100000) 

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
AB = AB[::-1]
res = (N*(N-1))//2
ans = []
for l in AB:
    l[0] -= 1
    l[1] -= 1
parent = [-1]*N


def root(node):
    if parent[node] < 0:
        return node
    else:
        parent[node] = root(parent[node])
        return parent[node]


def size(node):
    return -parent[root(node)]


def connect(a, b):
    a = root(a)
    b = root(b)
    if a == b:
        return False
    parent[a] += parent[b]
    parent[b] = a
    return True


for A, B in AB:
    ans.append(res)
    a = size(A)
    b = size(B)
    if connect(A, B):
        res -= a*b

for i in ans[::-1]:
    print(i)
