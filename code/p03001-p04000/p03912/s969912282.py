import sys, bisect, math, itertools, string, queue, copy
# import numpy as np
# import scipy
from collections import Counter,defaultdict,deque
from itertools import permutations, combinations
from heapq import heappop, heappush
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(input())
def inpm(): return map(int,input().split())
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())
def inplm(n): return list(int(input()) for _ in range(n))
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)]
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)])

def main():
    n,m = inpm()
    x = inpl()
    x.sort()
    ans = 0
    y = [0 for _ in range(n)]
    dic = defaultdict(int)
    dic2 = defaultdict(int)
    dic3 = defaultdict(int)
    for i in range(n):
        y[i] = x[i]%m
        dic[y[i]] += 1
        dic2[x[i]] += 1
    for e in dic2:
        if dic2[e]>1:
            dic3[e%m] += dic2[e]//2
    for i in range(m):
        if i > m-i:
            break
        elif i == 0:
            ans += dic[i]//2
        elif i == m/2:
            ans += dic[i]//2
        else:
            ans += min(dic[i],dic[m-i])
            if dic[i] == dic[m-i]:
                continue
            elif dic[i] > dic[m-i]:
                a = (min(dic[i]-dic[m-i],dic3[i]*2))//2
                if a>0:
                    ans += a
            elif dic[i] < dic[m-i]:
                a = (min(dic[m-i]-dic[i],dic3[m-i]*2))//2
                if a>0:
                    ans += a
    print(ans)
    
if __name__ == "__main__":
    main()