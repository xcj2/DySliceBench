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

def sqrt(x):
    epsilon = 10**(-15)
    guess = x / 2.0
    while abs(guess**2-x)>=epsilon:
        guess = guess - ((guess**2-x)/(2*guess))
    return guess


def main():
    a, b, c = LI()
    if 4 * a * b < (c - a - b) ** 2 and c - a - b >= 0:
        print('Yes')
    else:
        print('No')

main()

