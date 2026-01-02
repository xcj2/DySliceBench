N, M = map(int, input().split())
P = [int(p) for p in input().split()]

Par = [int(i) for i in range(N+1)]
Rank = [0 for i in range(N+1)]

def find(i, Par):
    if Par[i] == i:
        return i
    else:
        Par[i] = find(Par[i], Par)
        return Par[i]
def Unite(x, y):
    rx, ry = find(x, Par), find(y, Par)
    if rx == ry: return
    if Rank[rx] < Rank[ry]: Par[rx] = ry
    else: 
        Par[ry] = rx
        if Rank[rx] == Rank[ry]: Rank[rx] += 1
def Same(x, y): return find(x, Par) == find(y, Par)
    

for i in range(M):
    x, y = map(int, input().split())
    x, y = min(x, y), max(x, y)
    Unite(x, y)
    
Count = 0
for i in range(N):
    Count += (1 if Same(P[i], i+1) else 0)
print(Count)