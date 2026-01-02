import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
     
def main():
    arr = LI()
    arr = sorted(arr)
    mod2_arr = [0, 0, 0]
    for i, a in enumerate(arr):
        mod2_arr[i] = a % 2

    if sum(mod2_arr) == 0 or sum(mod2_arr) == 3:
        ans = 0

    elif sum(mod2_arr) == 1:
        for i, a in enumerate(arr):
            if arr[i] % 2 == 0:
                arr[i] += 1
        arr = sorted(arr)
        ans = 1
    else:
        for i, a in enumerate(arr):
            if arr[i] % 2 == 1:
                arr[i] += 1
        arr = sorted(arr)
        ans = 1
    ans += (arr[2] - arr[0]) // 2 + (arr[2] - arr[1]) // 2
    print(ans)
main()

