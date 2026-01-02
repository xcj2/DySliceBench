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
    N = I()
    A = LI()
    freq = [0] * (10**5)
    for a in A:
        freq[a] += 1
    ans = -1
    for i in range(len(freq)):
        if i == 0:
            l = 0
        else:
            l = freq[i-1]

        m = freq[i]

        if i == len(freq)-1:
            r = 0
        else:
            r = freq[i+1]
        ans = max(ans, l + m + r)
    print(ans)
main()

