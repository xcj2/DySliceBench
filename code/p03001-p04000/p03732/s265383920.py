from collections import Counter,defaultdict,deque
import sys
import bisect
import math
import itertools
import string
import queue
import copy
from itertools import permutations, combinations
from heapq import heappop, heappush
# input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
 
def inp(): # n=1
    return int(input())
def inpm(): # x=1,y=2
    return map(int,input().split())
def inpl(): # a=[1,2,3,4,5,...,n]
    return list(map(int, input().split()))
def inpls(): # a=['1','2','3',...,'n']
    return list(input().split())
def inplm(n): # x=[] 複数行
    return list(int(input()) for _ in range(n))
def inpll(n): # [[1,1,1,1],[2,2,2,2],[3,3,3,3]]
    return [list(map(int, input().split())) for _ in range(n)]

def main():
    n,W = inpm()
    v = [[] for _ in range(4)]
    w0 = 0
    for i in range(n):
        wv = inpl()
        if i == 0:
            w0 = wv[0]
        v[ wv[0]-w0 ].append(wv[1])
    for i in range(4):
        v[i] = sorted(v[i])
        v[i].reverse()
        vv = [0 for _ in range(len(v[i])+1)]
        for j in range(len(v[i])):
            vv[j+1] = vv[j] + v[i][j]
        v[i] = vv
    ans = 0
    for n1 in range(len(v[0])):
        for n2 in range(len(v[1])):
            for n3 in range(len(v[2])):
                for n4 in range(len(v[3])):
                    if W < w0*(n1+n2+n3+n4) + n2 + n3*2 + n4*3:
                        continue
                    ans = max(ans,v[0][n1]+v[1][n2]+v[2][n3]+v[3][n4])
    print(ans)

if __name__ == "__main__":
    main()