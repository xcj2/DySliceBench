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
    A, B, M = MI()
    a = LI()
    b = LI()
    xyc = LIR(M)
    
    m = min([a[i[0]-1] + b[i[1]-1] - i[2] for i in xyc])
    print(min([m, min(a)+min(b)]))

if __name__ == '__main__':
    main()