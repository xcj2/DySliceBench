#http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_B&lang=ja

def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

n = INT()
adj = [None]
for _ in range(n):
    adj_i = list(map(int, input().split()[2:]))
    adj.append(adj_i)

sndf = [None]
for i in range(1, n+1):
    sndf.append([False, i])

path = []

time = 0

def dfs(u):
    global time
    sndf[u][0] = True
    time += 1
    sndf[u].append(time)

    for v in adj[u]:
        if not sndf[v][0]:
            dfs(v)
    time += 1
    sndf[u].append(time)

for i in range(1, n+1):
    if not sndf[i][0]:
        dfs(i)

for x in sndf[1:]:
    print(*x[1:])


