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
    if n == 1 and m == 0:
        print(0)
        return
    check = [-1 for _ in range(n)]
    flag = True
    for _ in range(m):
        s,c = inpm()
        if check[s-1] == -1:
            check[s-1] = c
        elif check[s-1] == c:
            continue
        else:
            flag = False
    if not flag:
        print(-1)
        return
    if n > 1 and check[0] == 0:
        print(-1)
        return
    for i in range(n):
        if check[i] == -1:
            if i == 0:
                check[i] = str(1)
            else:
                check[i] = str(0)
        else:
            check[i] = str(check[i])
    print(''.join(check))

if __name__ == "__main__":
    main()