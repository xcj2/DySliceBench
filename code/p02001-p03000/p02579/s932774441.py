import bisect, copy, heapq, math, sys
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
def celi(a,b):
    return -(-a//b)
sys.setrecursionlimit(5000000)
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]

def main():
    direction=[[1,0],[0,1],[-1,0],[0,-1]]


    h,w=map(int,input().split())
    c=tuple(map(int,input().split()))
    d=tuple(map(int,input().split()))
    s=[input() for i in range(h)]

    itta=[[-1]*w for i in range(h)]
    itta[c[0]-1][c[1]-1]=0
    de=deque([(c[0]-1,c[1]-1)])
    # print(d)
    cnt=0
    while de:
        lst=[]
        while de:
            now=de.popleft()
            flag=0
            for i in range(4):
                nh,nw=now[0]+direction[i][0],now[1]+direction[i][1]
                if 0<=nh<h and 0<=nw<w:
                    if itta[nh][nw]==-1 and s[nh][nw]==".":
                        itta[nh][nw]=cnt
                        de.append((nh,nw))
                    elif s[nh][nw]=="#" and flag==0:
                        flag=1
                        lst.append(now)
        # print(lst)
        for i in range(len(lst)):
            for j in range(5):
                for k in range(5):
                    nh,nw=lst[i][0]-2+j,lst[i][1]-2+k
                    if 0<=nh<h and 0<=nw<w and s[nh][nw]=="." and itta[nh][nw]==-1:
                        itta[nh][nw]=cnt+1
                        de.append((nh,nw,cnt+1))
        cnt+=1
    print(itta[d[0]-1][d[1]-1])

main()