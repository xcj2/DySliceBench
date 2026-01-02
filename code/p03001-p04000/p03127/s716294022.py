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
     
def count_zero(arr):
    cnt = 0
    for a in arr:
        if a == 0:
            cnt += 1

    return cnt
def main():
    N = I()
    a = LI()
    min_element = inf
    min_ix = -1
    while True:
        prev_min = min_element
        for i in range(N):
            if 0 < a[i] < min_element:
                min_element = a[i]
                min_ix = i
        if count_zero(a) == N-1:
            break
        for i in range(N):
            if i == min_ix:
                continue
            a[i] %= min_element
    print(prev_min)
main()

