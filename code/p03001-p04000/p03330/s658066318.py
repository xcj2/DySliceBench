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
for y in range(n):
    for x in range(n):
        if (x+y+2) % 3 == 0:
            d0[c[x][y]] += 1
        elif (x+y+2) % 3 == 1:
            d1[c[x][y]] += 1
        else:
            d2[c[x][y]] += 1
# print(d0)
# print(d1)
# print(d2)
res0 = []
res1 = []
res2 = []
for i in range(C):
    tmp = 0
    for key in d0.keys():
        tmp += d[key-1][i] * d0[key]
    res0.append([i,tmp])
    tmp = 0
    for key in d1.keys():
        tmp += d[key-1][i] * d1[key]
    res1.append([i,tmp])
    tmp = 0
    for key in d2.keys():
        tmp += d[key-1][i] * d2[key]
    res2.append([i,tmp])
res0.sort(key=lambda x:x[1])
res1.sort(key=lambda x:x[1])
res2.sort(key=lambda x:x[1])
# print(res0)
# print(res1)
# print(res2)
ans = mod
for i in range(3):
    for j in range(3):
        for k in range(3):
            if res0[i][0] == res1[j][0] or res0[i][0] == res2[k][0] or res2[k][0] == res1[j][0]:
                continue
            ans = min(res0[i][1]+res1[j][1]+res2[k][1], ans)
print(ans)            