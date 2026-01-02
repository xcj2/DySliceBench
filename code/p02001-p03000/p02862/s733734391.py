def com(N,K,mod):
    n=N
    K=min(K,N-K)
    k=K
    X=1  #分子
    Y=1  #分母
    for _ in range(K):
        X*=n
        X%=mod
        n-=1
    for _ in range(K):
        Y*=k
        Y%=mod
        k-=1
    Y=loop_pow(Y,mod-2,mod)  #Y**(mod-2) mod(mod)
    return X*Y%mod  #nCk mod(mod)

def loop_pow(x,n,mod):
    if n==0:
        return 1
    if n%2==0:
        t=loop_pow(x,n//2,mod)
        return (t*t)%mod
    return x*loop_pow(x,n-1,mod)%mod

def main():
    X,Y=map(int,input().split())
    if (X+Y)%3!=0:
        print(0)
    else:
        n=(2*Y-X)//3
        m=(2*X-Y)//3
        if n<0 or m<0:
            print(0)
        else:
            mod=10**9+7
            print(com(n+m,n,mod))

if __name__=="__main__":
    main()