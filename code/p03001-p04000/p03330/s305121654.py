import sys, bisect, math, itertools, string, queue, copy
# import numpy as np
# import scipy
from collections import Counter,defaultdict,deque
from itertools import permutations, combinations
from heapq import heappop, heappush
# input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(input()) # n=1
def inpm(): return map(int,input().split()) # x=1,y=2
def inpl(): return list(map(int, input().split())) # a=[1,2,3,4,5,...,n]
def inpls(): return list(input().split())  # a=['1','2','3',...,'n']
def inplm(n): return list(int(input()) for _ in range(n)) # x=[] 複数行
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)] # [[2,2,2,2],[1,1,1,1],[3,3,3,3]] 
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)]) # [[1,1,1,1],[2,2,2,2],[3,3,3,3]] 
def graph():
    n=inp()
    g=[[] for _ in range(n)]
    for i in range(n):
        a = inp()
        a -= 1
        g[i].append(a)
        g[a].append(i)
    return n,g

def main():
    n,c = inpm()
    D = inpll(c)
    a = inpll(n)
    dic1 = defaultdict(int)
    dic2 = defaultdict(int)
    dic3 = defaultdict(int)
    for i in range(n):
        for j in range(n):
            if (i+j)%3 == 0:
                dic1[a[i][j]] += 1
            elif (i+j)%3 == 1:
                dic2[a[i][j]] += 1
            elif (i+j)%3 == 2:
                dic3[a[i][j]] += 1
    ANS = 10**10
    if n == 1:
        for e in range(c):
            x = e
            ans = 0
            for color1 in dic1:
                if color1 == x+1:
                    continue
                ans += dic1[color1] * D[color1-1][x]
            ANS = min(ANS,ans)
        print(ANS)
        return
    for e in permutations(range(c),3):
        [x, y, z] = e
        ans = 0
        for color1 in dic1:
            if color1 == x+1:
                continue
            ans += dic1[color1] * D[color1-1][x]
        for color2 in dic2:
            if color2 == y+1:
                continue
            ans += dic2[color2] * D[color2-1][y]
        for color3 in dic3:
            if color3 == z+1:
                continue
            ans += dic3[color3] * D[color3-1][z]
        ANS = min(ANS,ans)
    print(ANS)            

if __name__ == "__main__":
    main()