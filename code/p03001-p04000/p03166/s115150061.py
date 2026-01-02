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

# from functools import lru_cache


def main():
    N, M = LI()
    es = [[x for x in LI()] for _ in range(M)]

    from collections import defaultdict
    outs = defaultdict(list)  # ノードが int なら、[[] for _ in range(n+1)] でもよさそう。
    # ins = defaultdict(int)    # ノードが int なら、 [0 for _ in range(n+1)] でもよさそう。
    for from_v, to_v in es:
        outs[from_v].append(to_v)
        # ins[to_v] += 1

    # @lru_cache()
    memo = [None for _ in range(N+1)]
    def max_len(v):
        if memo[v] is not None:
            return memo[v]

        if not outs[v]:
            memo[v] = 0
            return 0
        else:
            memo[v] = max([max_len(x)+1 for x in outs[v]])
            return memo[v]

    print(max([max_len(x) for x in range(1,N+1)]))


main()