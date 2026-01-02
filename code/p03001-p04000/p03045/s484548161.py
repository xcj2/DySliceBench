import sys
sys.setrecursionlimit(100000)

N, M = [int(x) for x in input().split()]

# Union Find
# N = 100
PARENT = list(range(N))

def root(n):
    if PARENT[n] == n:
        return n
    else:
        ret = root(PARENT[n])
        PARENT[n] = ret
        return ret

def same(n1, n2):
    return root(n1) == root(n2)

def unite(n1, n2):
    n1 = root(n1)
    n2 = root(n2)
    if n1 == n2:
        return
    PARENT[n1] = n2

used = set()

for i in range(M):
    x, y, z = [int(x) for x in input().split()]
    x -= 1
    y -= 1
    unite(x, y)

cnt = 0
for i,p in enumerate(PARENT):
    if root(p) == i:
        cnt += 1
print(cnt)
