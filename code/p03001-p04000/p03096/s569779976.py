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

def main():
    N = II()
    C = []
    for _ in range(N):
        c = II()
        if len(C) == 0 or c != C[-1]:
            C.append(c)
    global ans
    ans = 0
    dp = [1] + [0] * N
    from collections import defaultdict
    cnt_clr = defaultdict(int)
    for i, c in enumerate(C):
        ret = dp[i]
        ret += cnt_clr[c]
        cnt_clr[c] = ret
        dp[i + 1] = ret % MOD

    ans = dp[len(C)]

    return ans % MOD

print(main())