import sys
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()
from itertools import accumulate

def main():
    N, K = LI()
    V = LI()
    acc = [0] + list(accumulate(V))
    ans = 0
    for i in range(min(N, K) + 1):
        for p in range(i + 1):
            tmp = acc[p] + (acc[-1] - acc[-(i - p + 1)])
            sub = sorted(V[:p] + V[N - (i - p):])
            for s in sub[:K - i]:
                if s >= 0:
                    break
                tmp -= s
            ans = max(ans, tmp)
    return ans

print(main())