import sys, bisect, math, itertools, string, queue, copy
# import numpy as np
# import scipy
from collections import Counter,defaultdict,deque
from itertools import permutations, combinations
from heapq import heappop, heappush
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(input()) # n=1
def inpm(): return map(int,input().split()) # x=1,y=2
def inpl(): return list(map(int, input().split())) # a=[1,2,3,4,5,...,n]
def inpls(): return list(input().split())  # a=['1','2','3',...,'n']
def inplm(n): return list(int(input()) for _ in range(n)) # x=[] 複数行
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)] # [[1,1,1,1],[2,2,2,2],[3,3,3,3]] 
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
    h,w = inpm()
    a = inplT(h)
    dic = defaultdict(int)
    for i in range(h):
        for j in range(w):
            x = ord(a[i][j])
            dic[x] += 1
    aaa = 0
    q = 0
    for e in dic:
        if dic[e] != 1 and dic[e]%2 == 1:
            aaa += 1
            q = dic[e]
            if aaa == 2:
                print('No')
                return
    if h%2 == 0 and w%2 == 0:
        for e in dic:
            if dic[e]%4 != 0:
                print('No')
                return
    if (h%2 == 0 and w%2 == 1) or (h%2 == 1 and w%2 == 0):
        cnt = 0
        if aaa:
            print('No')
            return
        else:
            for e in dic:
                if dic[e]%2 != 0:
                    print('No')
                    return
                if dic[e]%4 == 2:
                    cnt += 1
            if h%2 == 0:
                key = h//2
            else:
                key = w//2
            if (key-cnt) < 0 or (key-cnt)%2 != 0:
                print('No')
                return
    if h%2 == 1 and w%2 == 1:
        cnt1 = 0
        cnt2 = 0
        if aaa:
            for e in dic:
                if dic[e]%2 == 1:
                    cnt1 += 1
                elif dic[e]%4 == 2:
                    cnt2 += 1
            if cnt1 != 1:
                print('No')
                return
            key = (h//2) + (w//2)
            if (key-cnt2) < 0 or (key-cnt2)%2 != 0:
                print('No')
                return
        else:
            for e in dic:
                if dic[e] == 1:
                    cnt1 += 1
                elif dic[e]%4 == 2:
                    cnt2 += 1
            if cnt1 != 1:
                print('No')
                return
            q -= 1
            if q%4 == 2:
                cnt2 += 1
            key = (h//2) + (w//2)
            if (key-cnt2) < 0 or (key-cnt2)%2 != 0:
                print('No')
                return
    print('Yes')

if __name__ == "__main__":
    main()