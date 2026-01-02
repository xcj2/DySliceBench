def euclid(a:int,b:int)->(int,int):
    #return x,y s.t ax + by = gcd(a,b)
    #a > b >= 0
    if b == 0:
        return 1,0
    x,y = euclid(b,a%b)
    return y,x - y*(a // b)

def inverse(a:int,mod:int)->int:
    #gcd(p,b) == 1
    if mod > a:
        n,x = euclid(mod,a)
    else:
        x,n = euclid(a,mod)
    return x

def devide_mod(a:int,b:int,mod:int)->int:
    #a // b
    x = inverse(b,mod)
    return  (a*x)%mod

mod = 10**9 + 7


def com_init(mx:int ,mod:int)->list:
    fac = [1]*mx
    inv = [1]*mx
    finv = [1]*mx
    for i in range(2,mx):
        fac[i] = fac[i - 1]*i%mod
        inv[i] = mod - inv[mod%i]*(mod//i)%mod
        finv[i] = finv[i-1]*inv[i]%mod
    return fac,finv,inv

fac,finv ,inv = com_init(10**5,10**9 + 7)

def com(n:int, k:int):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n]*(finv[k]*finv[n-k]%mod)%mod

def main():
    N, K = map(int,input().split())
    for i in range(1, K + 1 ):
        print(com(N - K + 1,i)*com(K - 1, i - 1)%mod)
    return


if __name__ == "__main__":
    main()