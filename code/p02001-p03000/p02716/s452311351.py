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
    inf=10**16
    n=II()
    aa=LI()
    if n%2:
        dp=[[-inf]*3 for _ in range(n)]
        dp[0][2]=0
        dp[0][0]=aa[0]
        dp[1][1]=aa[1]
        for i,a in enumerate(aa[2:],1):
            if i-1>=0:dp[i+1][0]=dp[i-1][0]+a
            if i-2>=0:dp[i+1][1]=max(dp[i-2][0],dp[i-1][1])+a
            elif i-1>=0:dp[i+1][1]=dp[i-1][1]+a
            if i-3>=0:dp[i+1][2]=max(dp[i-3][0],dp[i-2][1],dp[i-1][2])+a
            elif i - 2 >= 0: dp[i + 1][2] = max(dp[i - 2][1], dp[i - 1][2]) + a
            elif i - 1 >= 0: dp[i + 1][2] = dp[i - 1][2] + a
        ans=max(dp[-1][2],dp[-2][1])
        if n>2:ans=max(ans,dp[-3][0])
    else:
        dp=[[-inf]*2 for _ in range(n)]
        dp[0][0]=aa[0]
        dp[1][1]=aa[1]
        for i,a in enumerate(aa[2:],1):
            dp[i+1][0]=dp[i-1][0]+a
            if i-2>=0:dp[i+1][1]=max(dp[i-2][0],dp[i-1][1])+a
            elif i - 1 >= 0: dp[i + 1][1] = dp[i - 1][1] + a
        ans=max(dp[-1][1],dp[-2][0])
    print(ans)

main()