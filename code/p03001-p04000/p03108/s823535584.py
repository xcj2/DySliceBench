N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(M)]

answer = [N*(N-1)//2]
par = [-1] * (N+1)

def find(x):
    if par[x] < 0:
        return x
    else:
        return find(par[x])

def size(x):
    return -par[find(x)]

def unite(u, v):
    u = find(u)
    v = find(v)
    if u != v:
        if size(u) < size(v):
            u, v = v, u
        par[u] += par[v]
        par[v] = u


for d in data[::-1]:
    if find(d[0]) != find(d[1]):
        answer.append(answer[-1]-(size(d[0])*size(d[1])))
        unite(d[0], d[1])
    else:
        answer.append(answer[-1])

for i in answer[M-1::-1]:
    print(i)