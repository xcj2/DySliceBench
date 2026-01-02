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
    A, B, C, X, Y = LI()
    if X > Y:
        X, Y = Y, X
        A, B = B, A
    money_a_b = X * A + Y * B
    money_b_c = (Y - X) * B + (2 * X) * C
    money_c = Y * 2 * C
    ans = min(money_a_b, money_b_c, money_c)
    print(ans)

main()

