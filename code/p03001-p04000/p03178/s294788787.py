import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    md = 10 ** 9 + 7
    k = [int(c) for c in input()]
    n=len(k)
    d = int(input())
    dp = [[0] * d for _ in range(n)]
    for b in range(k[0]):
        dp[0][b % d] += 1
    border = k[0]
    dpi = dp[0]
    for i, a in enumerate(k[1:], 1):
        dpi1 = dpi
        dpi = dp[i]
        for j in range(d):
            pre = dpi1[j]
            if pre == 0: continue
            for b in range(10):
                nj = (j + b) % d
                dpi[nj] = (dpi[nj] + pre) % md
        for b in range(a):
            nj = (border + b) % d
            dpi[nj] += 1
        border = (border + a) % d

    #p2D(dp)
    ans = dp[n-1][0] - 1 + (border % d == 0)
    print(ans % md)

main()
