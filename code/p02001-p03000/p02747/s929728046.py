import sys; sys.setrecursionlimit(2147483647); input = sys.stdin.readline
from math import floor, ceil, sqrt, factorial, log
from collections import Counter, defaultdict, deque
from operator import itemgetter
INF = float('inf'); MOD = 10**9+7
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(MI())
def LIR(n): return [LI() for i in range(n)]
def IS(): return input().rstrip()
import re

def main():
    S = IS()
    if len(S)%2 == 1: print('No')
    elif 'hi'* (len(S)//2) == S: print('Yes')
    else: print('No')

if __name__ == '__main__':
    main()