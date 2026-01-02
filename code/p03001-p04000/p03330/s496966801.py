from collections import Counter,defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n,C = inpl()
d = []
c = []
for i in range(C):
    d.append(inpl())
for i in range(n):
    c.append(inpl())
d0 = defaultdict(int)
d1 = defaultdict(int)
d2 = defaultdict(int)
dd = [d0,d1,d2]
for y in range(n):
    for x in range(n):
        t = (x+y+2) % 3 
        dd[t][c[x][y]] += 1
# print(dd)
res = [[] for i in range(3)]
for i in range(C):
    for j in range(3):
        tmp = 0
        for key in dd[j].keys():
            tmp += d[key-1][i] * dd[j][key]
        res[j].append([i,tmp])   
for i in range(3):
    res[i].sort(key=lambda x:x[1])
# print(res)
ans = mod
for i in range(3):
    for j in range(3):
        for k in range(3):
            if res[0][i][0] == res[1][j][0] or res[0][i][0] == res[2][k][0] or res[2][k][0] == res[1][j][0]:
                continue
            ans = min(res[0][i][1]+res[1][j][1]+res[2][k][1], ans)
print(ans)            