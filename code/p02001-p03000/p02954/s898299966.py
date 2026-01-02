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
    s = S()
    l_min = 0
    l = 0
    ans = [0] * len(s)
    while l + 1 < len(s):
        r = l + 1
        if s[l] == 'R' and s[r] == 'L':
            r_max = r
            while s[r_max] == 'L':
                r_max += 1
                if r_max >= len(s):
                    break
            ans[l] = (l - l_min) // 2 + (r_max - 1- l) // 2 + 1
            ans[r] = r_max - l_min - ans[l]
            l_min = l = r_max
        else:
            l += 1
    for a in ans:
        print(a, end=' ')
    print()
main()

