import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
def input(): return sys.stdin.readline().rstrip()

def main():
    N,a,b=map(int,input().split())
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
    
    def COM(N,k):
        tmp=1
        k=min(k,N-k)
        for i in range(N,N-k,-1):
            tmp*=i
            tmp%=MOD
        for i in range(1,k+1):
            tmp*=modinv(i,MOD)
            tmp%=MOD
        return tmp
            
    ans=pow(2,N,MOD)-1-COM(N,a)-COM(N,b)
    while ans<0:
        ans+=+MOD
    print(ans)
    

if __name__ == '__main__':
    main()
