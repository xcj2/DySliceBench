#dpでできないかな？
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi
from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def SI(): return input().rstrip()
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod = 10**9 + 7

def dfs(x,tree,al):
    for i in tree[x]:
        if al[i]<0:
            al[i]=0
            dfs(i,tree,al)
    
        
def main():  
    n,m=MI()
    lis=[LI() for i in range(m)]
    #print(lis)
    cou=0
    for i in range(m):
        tree=[[] for i in range(n)]
        for j in range(m):
            if i!=j:
                tree[lis[j][0]-1].append(lis[j][1]-1)
                tree[lis[j][1]-1].append(lis[j][0]-1)
        count=0
        for k in range(n):
            al=[-1]*n
            al[k]=0
            dfs(k,tree,al)
            #print(al)
            if not -1 in al:
                count+=1
        if count!=n:
            cou+=1
    print(cou)    

if __name__ == '__main__':
    main()