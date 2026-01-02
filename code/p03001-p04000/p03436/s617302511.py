from collections import deque
from heapq import heapify,heappop,heappush,heappushpop
from copy import copy,deepcopy
from itertools import product,permutations,combinations,combinations_with_replacement
from collections import defaultdict,Counter
from bisect import bisect_left,bisect_right
from math import gcd,ceil,floor,factorial
# from fractions import gcd
from functools import reduce
from pprint import pprint
from statistics import mean,median,mode

INF = float("inf")

def mycol(data,col):
    return [ row[col] for row in data ]

def mysort(data,col,reverse_flag):
    data.sort(key=lambda x:x[col],reverse=reverse_flag)
    return data

def mymax(data):
    M = -1*float("inf")
    for i in range(len(data)):
        m = max(data[i])
        M = max(M,m)
    return M

def mymin(data):
    m = float("inf")
    for i in range(len(data)):
        M = min(data[i])
        m = min(m,M)
    return m

def mycount(ls,x):
    # lsはソート済みであること
    l = bisect_left(ls,x)
    r = bisect_right(ls,x)
    return (r-l)

def myoutput(ls,space=True):
    if space:
        if len(ls)==0:
            print(" ")
        elif type(ls[0])==str:
            print(" ".join(ls))
        elif type(ls[0])==int:
            print(" ".join(map(str,ls)))
        else:
            print("Output Error")
    else:
        if len(ls)==0:
            print("")
        elif type(ls[0])==str:
            print("".join(ls))
        elif type(ls[0])==int:
            print("".join(map(str,ls)))
        else:
            print("Output Error")

def I():
    return int(input())

def MI():
    return map(int,input().split())

def RI():
    return list(map(int,input().split()))

def CI(n):
    return [ int(input()) for _ in range(n) ]

def LI(n):
    return [ list(map(int,input().split())) for _ in range(n) ]

def S():
    return input()

def MS():
    return input().split()

def RS():
    return list(input())

def CS(n):
    return [ input() for _ in range(n) ]

def LS(n):
    return [ list(input()) for _ in range(n) ]

# ddict = defaultdict(lambda: 0)
# ddict = defaultdict(lambda: 1)
# ddict = defaultdict(lambda: int())
# ddict = defaultdict(lambda: list())
# ddict = defaultdict(lambda: float())

h,w = MI()
maze = LS(h)
sy = 1
sx = 1
gy = h
gx = w
sy -= 1
sx -= 1
gy -= 1
gx -= 1

d = [ [INF]*w for _ in range(h) ]

def bfs(sy,sx,gy,gx):
    q = deque()
    q.append([sy,sx])
    d[sy][sx] = 0
    while q:
        y,x = q.popleft()
        if y==gy and x==gx:
            break
        else:
            for j,i in ([1,0],[0,-1],[-1,0],[0,1]):
                ny = y + j
                nx = x + i
                if nx==-1 or ny==-1 or nx==w or ny==h:
                    pass
                elif maze[ny][nx]=="#":
                    pass
                elif d[ny][nx]!=INF:
                    pass
                else:
                    q.append([ny,nx])
                    d[ny][nx] = d[y][x] + 1
    return d[gy][gx]

count = 0
for i in range(h):
    c = maze[i].count('.')
    count += c

d = bfs(sy,sx,gy,gx) 
# print(f'd={d}')  
if d==INF:
    print('-1')
else:
    print(count-2-(d-1)) 