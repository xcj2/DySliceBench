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
    x, y = LI()
    diff = abs(abs(x) - abs(y))
    if x == 0:
        if y < 0:
            diff = -y + 1
        else:
            diff = y - x
        print(diff)
        return
    if y == 0:
        if x <= 0:
            diff = -x
        else:
            diff = x + 1
        print(diff)
        return

    if abs(x) < abs(y):
        if x < 0 and y < 0:
            diff += 2
        elif x > 0 and y > 0:
            diff += 0
        else:
            diff += 1
    else:
        if x < 0 and y < 0:
            diff += 0
        elif x > 0 and y > 0:
            diff += 2
        else:
            diff += 1
    print(diff)

main()

