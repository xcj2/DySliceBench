from heapq import heappop, heappush, heapify
import sys
input = lambda: sys.stdin.readline().rstrip()

def find(x):
    if parents[x] < 0:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]
def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    if parents[x] > parents[y]:
        x, y = y, x
    parents[x] += parents[y]
    parents[y] = x

def same(x, y):
    return find(x) == find(y)    

N = int(input())

verticies_x = []
verticies_y = []

for i in range(N):
    x, y = map(int, input().split())
    verticies_x.append((x,i))
    verticies_y.append((y,i))
verticies_x.sort()    
verticies_y.sort()

edge = []

for i in range(N-1):
    tmp_x = verticies_x[i+1][0] - verticies_x[i][0]
    tmp_y = verticies_y[i+1][0] - verticies_y[i][0]
    edge.append((tmp_x, verticies_x[i][1], verticies_x[i+1][1]))
    edge.append((tmp_y, verticies_y[i][1], verticies_y[i+1][1]))

ans = 0
edge.sort()
parents = [-1] * N
for cost, s, g in edge:
    if same(s,g):
        continue
    else:
        union(s,g)
        ans += cost
print(ans)