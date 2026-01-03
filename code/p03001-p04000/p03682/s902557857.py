import heapq
N = int(input())
town = []
for i in range(N):
    x, y = map(int, input().split())
    town.append((x, y, i))

uf = [i for i in range(N)]      #uf[i]==iであれば根

def root(x):
    if x == uf[x]:
        return x
    else:
        r = root(uf[x])
        uf[x] = r
        return r

def isSame(x,y):
    return root(x) == root(y)

def unite(x, y):
    x = root(x)
    y = root(y)
    if x==y:
        return
    uf[x] = y
    return

road = []
town.sort() #x座標でソート O(NlogN + N)
for i in range(N-1):
    x1, _, ind1 = town[i]
    x2, _, ind2 = town[i+1]
    cost = abs(x2 - x1)
    heapq.heappush(road, (cost, ind1, ind2))
town.sort(key = lambda x:x[1]) #y座標でソート O(NlogN + N)
for i in range(N-1):
    _, x1, ind1 = town[i]
    _, x2, ind2 = town[i+1]
    cost = abs(x2 - x1)
    heapq.heappush(road, (cost, ind1, ind2))

ans = 0
while road: #O(2N)
    cost, i, j = heapq.heappop(road)
    if isSame(i,j):
        continue
    unite(i, j)
    ans += cost

print(ans)
