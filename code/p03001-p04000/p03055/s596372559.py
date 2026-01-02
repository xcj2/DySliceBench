import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
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
        if directed == False:
            pt[t[i]-1].append(s[i]-1)
    return pt

def tree_diameter(pt):
    def bfs(pt,v):
        n = len(pt)
        visited = [False]*n
        visited[v] = True
        max_d = 0
        max_d_index = v
        q = [v]
        c = 1
        while q:
            q1 = []
            for i in q:
                for j in pt[i]:
                    if not visited[j]:
                        visited[j] = c
                        max_d = c
                        max_d_index = j
                        q1.append(j)
            q = q1
            c += 1
        return max_d, max_d_index
    
    _,index = bfs(pt,0)
    return bfs(pt,index)[0]

N = I()
a,b = LIR(N-1,2)

pt = edges_to_pt(a,b,N)
r = tree_diameter(pt)

# 木の直径 r（≥2）を -1 or -2 できる
# r = 1 をもらうと負け
if r%3 == 1:
    print('Second')
else:
    print('First')