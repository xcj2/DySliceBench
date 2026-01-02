import sys
from collections import defaultdict

int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    md=998244353
    n,s=MI()
    aa=LI()
    dp=[0]*(s+1)
    dp[0]=1
    inv=pow(2,md-2,md)
    for k,a in enumerate(aa):
        for i in range(s-a,-1,-1):
            dp[i+a]=(dp[i+a]+dp[i]*inv)%md
        #print(k,dp)
    ans=dp[s]*pow(2,n,md)%md
    print(ans)

main()