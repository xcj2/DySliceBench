import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def main():
    md=10**9+7
    n=II()
    xx=LI()
    fac=[1]*n
    for k in range(1,n):
        fac[k]=fac[k-1]*k%md
    rfac=[n-1]*n
    for k in range(n-2,-1,-1):
        rfac[k]=rfac[k+1]*k%md
    ans=0
    coff=0
    for i,(x0,x1) in enumerate(zip(xx,xx[1:]),1):
        d=x1-x0
        if i+1<n:coff+=fac[i-1]*rfac[i+1]
        else:coff+=fac[i-1]
        #print(coff)
        ans+=d*coff
        ans%=md
    print(ans)

main()