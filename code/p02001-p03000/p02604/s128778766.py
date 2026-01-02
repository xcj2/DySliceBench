import sys

int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def cal(xp):
    res=[inf]*(n+1)
    xp.sort()
    m=len(xp)
    dp=[[inf]*(m+1) for _ in range(m+1)]
    dp[0][0]=0
    for l,(x,p) in enumerate(xp):
        dp[l+1][0]=dp[l][0]+abs(x)*p
    for l in range(m):
        dpl=dp[l]
        for r in range(l+1,m+1):
            dpr=dp[r]
            val=inf
            for lx,_ in xp[l:r]:
                cur=0
                for x,p in xp[l:r]:
                    cur+=min(abs(x-lx),abs(x))*p
                val=min(cur,val)
            for j in range(1,m+1):
                dpr[j]=min(dpr[j],dpl[j-1]+val)
    dpm=dp[m]
    for i in range(m+1):res[i]=dpm[i]
    return res

inf = 10 ** 16
n = II()
xyp = LLI(n)
ans=[inf]*(n+1)
for s in range(1<<n):
    xp=[]
    yp=[]
    for i,(x,y,p) in enumerate(xyp):
        if s>>i&1:xp.append((x,p))
        else:yp.append((y,p))
    xc=cal(xp)
    yc=cal(yp)
    for i in range(n+1):
        for j in range(n+1-i):
            ans[i+j]=min(ans[i+j],xc[i]+yc[j])

for a in ans:print(a)
