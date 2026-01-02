from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

def FordFulkerson(S,T): #sからFord-Fulkerson
    global lines
    global cost
    global ans

    queue = deque()     #BFS用のdeque
    queue.append([S,INF])
    ed = [True]*N    #到達済み
    ed[S] = False
    route = [0 for i in range(N)]   #ルート
    route[S] = -1

    #BFS
    while queue:
        s,flow = queue.pop()
        for t in lines[s]:  #s->t
            if ed[t]:
                flow = min(cost[s][t],flow)  #flow = min(直前のflow,line容量)
                route[t] = s
                queue.append([t,flow])
                ed[t] = False
                if t == T: #ゴール到達
                    ans += flow
                    break
        else:
            continue
        break
    else:
        return False

    #ラインの更新
    t = T
    s = route[t]
    while s != -1:
        #s->tのコスト減少，ゼロになるなら辺を削除
        cost[s][t] -= flow
        if cost[s][t] == 0:
            lines[s].remove(t)

        #t->s(逆順)のコスト増加，元がゼロなら辺を作成
        if cost[t][s] == 0:
            lines[t].add(s)
        cost[t][s] += flow

        t = s
        s = route[t]
    return True

def PrimeFactoring(x):
    p = 2
    primes = []
    while x >= 2:
        if x%p == 0:
            primes.append(p)
            x //= p
            p = 2
        else:
            p += 1
    return primes

while True:
    X,Y,M = inpl()
    lines = defaultdict(set)
    N = X+Y+2
    S = X+Y
    T = X+Y+1
    cost = [[0]*N for _ in range(N)]

    for i in range(M):
        x,y = inpl()
        lines[x].add(y+X)
        cost[x][y+X] = 1
        
    for i in range(X):
        lines[S].add(i)
        cost[S][i] = 1
    for i in range(Y):
        lines[i+X].add(T)
        cost[i+X][T] = 1

    ans = 0

    while FordFulkerson(S,T):
        pass

    print(ans)

    break

