import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def MI(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

def edges_to_pt(s,t,n,directed=False):
    pt = [[] for _ in range(n)]
    for i in range(len(s)):
        pt[s[i]-1].append(t[i]-1)
        if directed==False:
            pt[t[i]-1].append(s[i]-1)
    return pt

def shortest_path(pt,s,t):
    n = len(pt)
    used = [False]*n
    pre = [-1]*n
    q = [s]
    while q:
        q1 = []
        for i in q:
            for j in pt[i]:
                if not used[j]:
                    used[j] = True
                    pre[j] = i
                    q1.append(j)
        q = q1

    if used[t]:
        path = [t]
        p = t
        while True:
            p = pre[p]
            path.append(p)
            if p == s:
                break
        return list(reversed(path))
    else:
        return []

N = I()
a,b = MI(N-1,2)

pt = edges_to_pt(a,b,N)
path = shortest_path(pt,0,N-1)

v = path[math.ceil(len(path)/2)]
visited = [False]*N
visited[v] = True
S = [v]
num = 1
while S:
    v1 = S.pop()
    for i in pt[v1]:
        if i == path[math.ceil(len(path)/2)-1]:
            continue
        if not visited[i]:
            visited[i] = True
            num += 1
            S.append(i)

if N-num > num:
    print('Fennec')
else:
    print('Snuke')