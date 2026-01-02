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
    x1, y1, x2, y2 = LI()
    d = max(abs(x1-x2), abs(y1-y2))
    dx = abs(x1-x2)
    dy = abs(y1-y2)
    if x1 < x2 and y1 <= y2:
        x3 = x2 - dy
        x4 = x1 - dy
        y3 = y2 + dx
        y4 = y1 + dx
    elif x1 < x2 and y1 > y2:
        x3 = x2 + dy
        x4 = x1 + dy
        y3 = y2 + dx
        y4 = y1 + dx
    elif x1 >= x2 and y1 < y2:
        x3 = x2 - dy
        x4 = x1 - dy
        y3 = y2 - dx
        y4 = y1 - dx
    else:
        x3 = x2 + dy
        x4 = x1 + dy
        y3 = y2 - dx
        y4 = y1 - dx
    print(x3, y3, x4, y4)



main()

