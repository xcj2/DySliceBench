import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from collections import deque

n, m = li()
graph = [[] for _ in range(n)]

ins = [0]*n
par = [0]*n

# 親をたどるグラフを作る
for _ in range(n-1+m):
    a,b = li_()
    graph[a].append(b)
    ins[b] += 1

# 入次数が尽きたものからスタートに
start = ins.index(0)
que = deque([start])
while que:
    cur = que.popleft()
    for child in graph[cur]:
        ins[child] -= 1
        if ins[child] == 0:
            que.append(child)
            par[child] = cur+1
    
for pi in par:
    print(pi)