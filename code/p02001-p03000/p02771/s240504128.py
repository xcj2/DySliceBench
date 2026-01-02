import sys; sys.setrecursionlimit(2147483647); input = sys.stdin.readline
from math import floor, ceil, sqrt, factorial, log
from collections import Counter, defaultdict
from operator import itemgetter
INF = float('inf'); MOD = 10**9+7
def I(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(MI())
def LIR(n): return [LI() for i in range(n)]
def S(): return input().rstrip()

def main():
    A, B, C = MI()
    if A==B and A!=C: print('Yes')
    elif A==C and A!=B: print('Yes')
    elif B==C and A!=C: print('Yes')
    else: print('No')
if __name__ == '__main__':
    main()