import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7 # 998244353
input=lambda:sys.stdin.readline().rstrip()
from itertools import product
def bisection(l,r,f,left=True,discrete=True):
    eps=1 if(discrete) else 10**-8
    if((not left)^f(r)): return r if(left) else r+1
    elif(left^f(l)): return l-1 if(left) else l
    while(r-l>eps):
        h=(l+r)//2 if(discrete) else (l+r)/2
        if((not left)^f(h)): l=h
        else: r=h
    return (l+r)/2 if(not discrete) else l if(left) else r

def resolve():
    k = int(input())

    def check(x):
        x = str(x)
        dp = [[0] * 2 for _ in range(10)]
        
        s = int(x[0])
        for i in range(1, s):
            dp[i][1] = 1
        dp[s][0] = 1

        x = x[1:]
        for s in x:
            s = int(s)
            ndp = [[0] * 2 for _ in range(10)]
            for d, lt in product(range(10), range(2)):
                for nd in [d-1, d, d+1]:
                    if not (0 <= nd <= 9):
                        continue
                    if lt == 0 and s < nd:
                        continue
                    nlt = max(lt, s > nd)
                    ndp[nd][nlt] += dp[d][lt]
            for d in range(1, 10):
                ndp[d][1] += 1
            dp = ndp
        return sum(dp[d][lt] for d, lt in product(range(10), range(2))) >= k

    print(bisection(1, 10**18+1, check, left=False))
resolve()