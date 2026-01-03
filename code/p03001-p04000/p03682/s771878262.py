import sys
sys.setrecursionlimit(500000)

N = int(input())
T = [[i] + list(map(int, input().split())) for i in range(N)]
E = [[] for i in range(N)]
E = []
T.sort(key=lambda x: x[1])
for i in range(N-1):
    s, l = T[i:i+2]
    E.append([s[0], l[0], l[1]-s[1]])
T.sort(key=lambda x: x[2])
for i in range(N-1):
    s, l = T[i:i+2]
    E.append([s[0], l[0], l[2]-s[2]])
E.sort(key=lambda x: x[2])

Par = list(range(N))
def root(x):
    if Par[x] == x:
        return x
    else:
        Par[x] = root(Par[x])
        return Par[x]

def same(x, y):
    return root(x) == root(y)

def unite(x, y):
    x = root(x)
    y = root(y)
    if x != y:
        Par[x] = y

ans = 0
for e in E:
    if not same(e[0], e[1]):
        ans += e[2]
        unite(e[0], e[1])

print(ans)
