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
    #aの大きい順に、左右どちらかの端から埋めていく
    n=II()
    aa=LI()
    dp=[[0]*(n+1) for _ in range(n+1)]
    #dp[l][r]...左からl人、右からr人埋まっているときの最大値
    for s,(i,a) in enumerate(sorted(enumerate(aa),key=lambda x:-x[1])):
        for l in range(s+1):
            r=s-l
            pre=dp[l][r]
            dp[l+1][r]=max(dp[l+1][r],pre+abs(l-i)*a)
            dp[l][r+1]=max(dp[l][r+1],pre+abs(n-1-r-i)*a)
    ans=0
    for l in range(n+1):
        ans=max(ans,dp[l][n-l])
    print(ans)

main()