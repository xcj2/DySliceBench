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

def main():
    X = I()
    a = 0
    if X >= 500:
        a += (X//500)*1000
        X = X%500
    if X >= 5:
        a += (X//5)*5
    print(a)

if __name__ == '__main__':
    main()