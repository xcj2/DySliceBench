from collections import Counter,defaultdict,deque
import sys
import bisect
import math
import itertools
import string
import queue
import copy
# import numpy as np
# import scipy
from itertools import permutations, combinations
from heapq import heappop, heappush
input = sys.stdin.readline
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
    return sorted([list(map(int, input().split())) for _ in range(n)])


def main():
    h,w=inpm()
    s=[input() for _ in range(h)]
    que=deque()
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    went = [[False for _ in range(w)] for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j]=="#":
                if not went[i][j]:
                    went[i][j] = True
                    que = deque()
                    que.append((i,j))
                    a,b = 1,0
                    while len(que)>0:
                        x,y=que.pop()
                        for k in range(4):
                            nx,ny=x+dx[k],y+dy[k]
                            if nx<0 or h<=nx or ny<0 or w<=ny or went[nx][ny]:
                                continue
                            if s[x][y] != s[nx][ny]:
                                if s[nx][ny] == '#':
                                    a+=1
                                else:
                                    b+=1
                                went[nx][ny]=True
                                que.append((nx,ny))
                    ans += a*b
    print(ans)
    
if __name__ == "__main__":
    main()