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
     

def iskaibun(s):
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
            continue
        else:
            return False
    return True

def main():
    s = S()
    N = len(s)
    if iskaibun(s) and iskaibun(s[:(N-1)//2]) and iskaibun(s[(N+3)//2 - 1:]):
        print('Yes')
    else:
        print('No')

main()

