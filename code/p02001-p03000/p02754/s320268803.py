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
    N, A, B = MI()
    ans = N//(A+B)*A
    rem = N%(A+B)
    print(ans+min(rem, A))
if __name__ == '__main__':
    main()