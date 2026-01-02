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

def div4(x): #素因数分解配列 dict格納型
    div=defaultdict(int)
    check=2
    while(x!=1 and check <= int(x**0.5)+2):
        while x%check==0:
            div[check]+=1
            x/=check
        check+=1
    if x != 1:
      div[x]+=1
    return div

def nCk(n,k):
    res = 1
    a=n-k
    b=k
    for i in range(1,a+b+1):
        res = res*i%mod
    for i in range(1,a+1):
        res = res*mod_inv(i,mod)%mod
    for i in range(1,b+1):                                 
        res = res*mod_inv(i,mod)%mod
    return res

def main():
    x,y,z,K = inpm()
    a = inpl()
    b = inpl()
    c = inpl()
    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)
    que = []
    for i in range(x):
        for j in range(y):
            for k in range(z):
                if (i+1)*(j+1)*(k+1)>K:
                    break
                else:
                    que.append(a[i]+b[j]+c[k])
    que.sort(reverse=True)
    for i in range(K):
        print(que[i])


if __name__ == "__main__":
    main()