from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

MAX = 10**5*2+3

N,K = inpl()
aa = inpl()
cnts = defaultdict(int)
inds = defaultdict(list)
info = [[0,0] for _ in range(N)]
ed = set(aa)

for i,a in enumerate(aa):
    cnts[a] += 1
    inds[a].append(i)     # inds[a][i-1] : a の i番目の index
    info[i] = [a,cnts[a]] # aa[i] -> info[i][1] 番目の info[i][0]


nexts = [-1]*MAX
ed.add(0)
for e in ed:
    tmp = e
    if e == 0:
        i = 0
    else:
        i = inds[tmp][0] + 1

    while True:
        #print(tmp,i)
        if i == N:
            nexts[e] = 0
            break
        tmp,n = info[i]
        if cnts[tmp] == n:
            nexts[e] = tmp
            break
        else: #cnts[a] != n
            nextind = inds[tmp][n+1-1] # tmpの値の次のindex
            nextind += 1 # の一個次
            i = nextind


visited = [False]*MAX
kero = []
x = 0
L = 0
while True:
    if visited[x]:
        break
    else:
        kero.append(x)
        visited[x] = True
        x = nexts[x]
        L += 1

tmp = kero[K%L-1]
#print(kero)
#print(tmp)

ans = []
if tmp == 0:
    i = 0
else:
    i = inds[tmp][0] + 1

while i < N:
    tmp,n = info[i]
    if cnts[tmp] == n:
        ans.append(tmp)
        i += 1
    else:
        nextind = inds[tmp][n+1-1] # tmpの値の次のindex
        nextind += 1 # の一個次
        i = nextind

print(' '.join(map(str,ans)))
