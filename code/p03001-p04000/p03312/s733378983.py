import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]
dij=[(1,0),(0,1),(-1,0),(0,-1)]

def main():
    n=II()
    aa=LI()

    pre=[0]*(n+1)
    for i in range(n):pre[i+1]+=pre[i]+aa[i]

    ll=[[0]*2 for _ in range(n)]
    rr=[[0]*2 for _ in range(n)]
    j=1
    for i in range(2,n-1):
        while j<i-1 and pre[i]-pre[j]*2>0:j+=1
        if pre[i]-pre[j-1]*2<-pre[i]+pre[j]*2:j-=1
        ll[i][0]=min(pre[i]-pre[j],pre[j])
        ll[i][1]=max(pre[i]-pre[j],pre[j])
    j=n-1
    for i in range(n-2,1,-1):
        while j>i+1 and pre[n]+pre[i]-pre[j]*2<0:j-=1
        if -pre[n]-pre[i]+pre[j+1]*2<pre[n]+pre[i]-pre[j]*2:j+=1
        rr[i][0]=min(pre[n]-pre[j],pre[j]-pre[i])
        rr[i][1]=max(pre[n]-pre[j],pre[j]-pre[i])
    #print(ll,rr)

    ans=10**16
    for i in range(2,n-1):
        mn=min(ll[i][0],rr[i][0])
        mx=max(ll[i][1],rr[i][1])
        cur=mx-mn
        if cur<ans:ans=cur
    print(ans)

main()