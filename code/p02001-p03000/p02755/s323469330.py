import sys; sys.setrecursionlimit(2147483647); input = sys.stdin.readline
from math import floor, ceil, sqrt, factorial, log
from collections import Counter, defaultdict
from operator import itemgetter
INF = float('inf'); MOD = 10**9+7
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(MI())
def LIR(n): return [LI() for i in range(n)]
def S(): return input().rstrip()

def main():
    A, B = MI()
    for i in range(1009):
        if int(i*0.08) == A and int(i*0.1) == B: print(i); sys.exit()
    print(-1)
if __name__ == '__main__':
    main()