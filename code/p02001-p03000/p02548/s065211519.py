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
    ans = 0
    for a in range(1, 10**3+1):
        if a ** 2 >= N:
            continue
        b_num = N // a - a
        if a * (N // a) == N:
            b_num -= 1
        ans += b_num
    ans *= 2
    ans += int(math.sqrt(N))
    if int(math.sqrt(N)) ** 2 == N:
        ans -= 1
    print(ans)
main()

