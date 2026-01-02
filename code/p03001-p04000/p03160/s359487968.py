import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
INF = 10 ** 18
MOD = 10 ** 9 + 7

from functools import lru_cache

def main(): 
    N = II()
    h = LI()

    # @lru_cache()
    # def min_cost(x):
    #     if x == 0: return 0
    #     elif x == 1: return abs(h[1] - h[0])
    #     else: return min(min_cost(x-1) + abs(h[x] - h[x-1]), min_cost(x-2) + abs(h[x] - h[x-2]))

    min_cost = [0 for _ in range(N)]
    min_cost[0] = 0
    min_cost[1] = abs(h[1] - h[0])
    for x in range(2, N):
        min_cost[x] = min(min_cost[x-1] + abs(h[x] - h[x-1]), min_cost[x-2] + abs(h[x] - h[x-2]))

    print(min_cost[N-1])

main()