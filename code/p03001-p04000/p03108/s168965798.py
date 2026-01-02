from collections import defaultdict
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())


def Find(x):    #xの根を返す
    global table

    if table[x] == x:
        return x
    else:
        table[x] = Find(table[x])    #親の更新(根を直接親にして参照距離を短く)
        size[x] = size[table[x]]
        return table[x]

def Unite(x,y):    #xとyを繋げる
    global size
    global rank
    x = Find(x)
    y = Find(y)
    sx = Size(x)
    sy = Size(y)

    if x == y:
        return

    if rank[x] > rank[y]:
        table[y] = x
        size[x] = sx + sy
    else:
        table[x] = y
        size[y] = sx + sy
        if rank[x] == rank[y]:
            rank[y] += 1

def Check(x,y):
    if Find(x) == Find(y):
        return True
    else:
        return False

def Size(x):
    return size[Find(x)]

N,M = inpl()

table = [i for i in range(N)]    #木の親 table[x] == x なら根
rank  = [1 for i in range(N)]    #木の長さ
size  = [1 for i in range(N)]

ABs = [inpl() for i in range(M)]
ans = N*(N-1)//2
ans_list = [ans]

for A,B in reversed(ABs):
    A -= 1
    B -= 1
    #print(A,B,Size(A),Size(B))
    if not Check(A,B):
        ans -= Size(A) * Size(B)
        Unite(A,B)
    ans_list.append(ans)

for i in reversed(range(M)):
    print(ans_list[i])
