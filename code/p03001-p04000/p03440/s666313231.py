from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)
N, M = map(int, input().split())
if N - 1 == M:
    print(0)
    exit()
if N < 2 * (N - M - 1):
    print('Impossible')
    exit()


parent = [i for i in range(N)]
rank = [0] * N


def find(i):
    if parent[i] == i:
        return i
    else:
        parent[i] = find(parent[i])
        return parent[i]


def same(x, y):
    return find(x) == find(y)


def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return

    if rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


A = list(map(int, input().split()))
G = [[] for i in range(N)]
X, Y = [], []
for i in range(M):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
    unite(x, y)

K = 0
D = defaultdict(list)
for i in range(N):
    k = find(i)
    if not D[k]:
        K += 1
    D[k].append((A[i], i))

ans = 0
used = [0] * N
for v in D.values():
    s = min(v)
    ans += s[0]
    used[s[1]] = 1

T = []
for i in range(N):
    if not used[i]:
        T.append(A[i])

T = sorted(T)
ans += sum(T[:2 * (N - M - 1) - K])
print(ans)
