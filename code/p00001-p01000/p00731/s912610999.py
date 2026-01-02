from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

def cal(x,y,f):
    return (x+y*W)*2+f

def dijkstra(lines,N,s):
    weight = [INF]*N
    weight[s] = 0
    def search(s,w_0,q,weight):
        for t,w in lines[s]:
            w += w_0
            if weight[t] > w:
                heapq.heappush(q,[w,t])
                weight[t] = w
    q = [[0,s]]
    heapq.heapify(q)
    while q:
        w,n = heapq.heappop(q)
        search(n,w,q,weight)
    return weight


dxr = [ 1, 1, 1, 1, 1, 2, 2, 2, 3]
dyr = [-2,-1, 0, 1, 2,-1, 0, 1, 0]

dxl = [-1,-1,-1,-1,-1,-2,-2,-2,-3]
dyl = [-2,-1, 0, 1, 2,-1, 0, 1, 0]

while True:
    W,H = inpl()
    if W == 0:
        break
    ss = [list(input().split()) for _ in range(H)]

    N = W*H*2+2
    S = W*H*2
    T = W*H*2+1
    lines = defaultdict(set)
    for x in range(W):
        for y in range(H):
            if ss[y][x] == 'S':
                lines[S].add((cal(x,y,0),0))
                lines[S].add((cal(x,y,1),0))
            if ss[y][x] == 'T':
                lines[cal(x,y,0)].add((T,0))
                lines[cal(x,y,1)].add((T,0))
                continue
            if ss[y][x] == 'X':
                continue
            else:
                f = 0 # 次が右足
                for i in range(9):
                    tx = x + dxr[i]
                    ty = y + dyr[i]
                    if (0 <= tx < W) and (0 <= ty < H):
                        if ss[ty][tx] == 'S' or ss[ty][tx] == 'T':
                            cost = 0
                        elif ss[ty][tx] == 'X':
                            continue
                        else:
                            cost = int(ss[ty][tx])
                        lines[cal(x,y,0)].add((cal(tx,ty,1),cost))

                f = 1 # 次が左足
                for i in range(9):
                    tx = x + dxl[i]
                    ty = y + dyl[i]
                    if (0 <= tx < W) and (0 <= ty < H):
                        if ss[ty][tx] == 'S' or ss[ty][tx] == 'T':
                            cost = 0
                        elif ss[ty][tx] == 'X':
                            continue
                        else:
                            cost = int(ss[ty][tx])
                        lines[cal(x,y,1)].add((cal(tx,ty,0),cost))

    weights = dijkstra(lines,N,S)
    if weights[T] == INF:
        print(-1)
    else:
        print(weights[T])

