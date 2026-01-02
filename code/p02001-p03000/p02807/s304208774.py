import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
def input():
    return sys.stdin.readline().rstrip()

def main():
    def modinv(a, mod):
        b,u,v = mod,1,0
        while b:
            t=a//b
            a-=t*b
            a,b=b,a
            u-=t*v
            u,v=v,u
        u%=mod
        if u < 0:
            u+=mod
        return u
    
    N=int(input())
    x=list(map(int,input().split()))
    z=[0]*N
    z[0]=1
    for i in range(N-1):
        z[0]*=i+1
        z[0]%=MOD
    ans=0
    for i in range(N-1):
        ans+=(x[i+1]-x[i])*z[i]
        ans%=MOD
        z[i+1]=z[i]+z[0]*modinv(i+2,MOD)
        z[i+1]%=MOD
    print(ans)

if __name__ == '__main__':
    main()
