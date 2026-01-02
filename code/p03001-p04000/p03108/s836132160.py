import sys
input = lambda: sys.stdin.readline().rstrip()
import math

N, M = map(int, input().split())

def find(x):
    if parents[x] < 0:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if parents[x] > parents[y]:
        x,y = y, x

    parents[x] += parents[y]
    parents[y] = x 

def same(x,y):
    return find(x) == find(y)

def parent_count(x):
    return -parents[find(x)]

edges = []
for i in range(M):
    a, b = map(int, input().split())
    edges.append((a-1,b-1))

ans = [0] * (M+1)
parents = [-1] * N
ans[-1] = N*(N-1)//2

for i in range(M-1, -1, -1):
    s, e = edges[i]
    if same(s, e):
        ans[i] = ans[i+1]
    else:
        ans[i] = ans[i+1] - parent_count(s) * parent_count(e)
        union(s, e)
        
for i in range(1,M+1):
  	print(ans[i])