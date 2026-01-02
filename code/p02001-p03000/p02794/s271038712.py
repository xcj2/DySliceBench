import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())

N = I()
dist = [[100]*(N+1) for _ in range(N+1)]  # 2点間の最短距離
edges = {}

for i in range(N-1):
    a,b = MI()
    dist[a][b] = 1
    dist[b][a] = 1
    edges[(a,b)] = i
    edges[(b,a)] = i

for i in range(1,N+1):
    dist[i][i] = 0

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])

M = I()
A = []  # uとvを結ぶ経路上にある辺の集合
for _ in range(M):
    u,v = MI()
    B = set()
    while True:
        if dist[u][v] == 1:
            B.add(edges[(u,v)])
            break
        else:
            for i in range(1,N+1):
                if dist[u][i] == dist[u][v]-1 and dist[i][v] == 1:
                    B.add(edges[(i,v)])
                    v = i
                    break
    A.append(B)


def popcount(n):
    c = (n & 0x5555555555555555) + ((n >> 1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c >> 2) & 0x3333333333333333)
    c = (c & 0x0f0f0f0f0f0f0f0f) + ((c >> 4) & 0x0f0f0f0f0f0f0f0f)
    c = (c & 0x00ff00ff00ff00ff) + ((c >> 8) & 0x00ff00ff00ff00ff)
    c = (c & 0x0000ffff0000ffff) + ((c >> 16) & 0x0000ffff0000ffff)
    c = (c & 0x00000000ffffffff) + ((c >> 32) & 0x00000000ffffffff)
    return c


# 包除原理

ans = 0
for i in range(2**M):
    C = set()
    for j in range(M):
        if (i >> j) & 1:
            C |= A[j]
    l = len(C)
    a = popcount(i)
    a %= 2
    ans += (-1)**a * 2**(N-1-l)

print(ans)
