def loop_pow(x,n,mod):
    if n==0:
        return 1
    if n%2==0:
        t=loop_pow(x,n//2,mod)
        return (t*t)%mod
    return x*loop_pow(x,n-1,mod)%mod

def com(N,K,mod):
    n=N
    k=K
    up=1
    down=1
    for _ in range(K):
        up*=n
        up%=mod
        n-=1
    for _ in range(K):
        down*=k
        down%=mod
        k-=1
    down=loop_pow(down,10**9+5,mod)
    return up*down%mod

def main():
    N,a,b=map(int,input().split())
    mod=10**9+7
    t=(loop_pow(2,N,mod)-1-com(N,a,mod)-com(N,b,mod))%mod
    print(t)

if __name__=="__main__":
    main()