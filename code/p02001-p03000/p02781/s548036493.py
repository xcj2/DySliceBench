import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    s=SI()
    k=II()
    n=len(s)
    dp=[[[0]*2 for _ in range(k+1)] for _ in range(n+1)]
    dp[0][0][0]=1
    # dp[i][j][f]...i桁目までみたとき、0でない数字がj個で、s以下が確定かどうかがf
    for i,c in enumerate(s):
        for j in range(k+1):
            for f in range(2):
                pre=dp[i][j][f]
                if pre==0:continue
                if f:
                    dp[i+1][j][f]+=pre
                    if j<k:dp[i+1][j+1][f]+=pre*9
                else:
                    c=int(c)
                    if c:
                        dp[i+1][j][1]+=pre
                        if j<k:
                            dp[i+1][j+1][1]+=pre*(c-1)
                            dp[i+1][j+1][0]+=pre
                    else:
                        dp[i+1][j][0]+=pre
    print(sum(dp[n][k]))

main()