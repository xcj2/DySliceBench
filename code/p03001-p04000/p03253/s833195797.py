mod = 10**9+7
def prime(n,p):
    iteral = 0
    while n%p == 0:
        n //= p
        iteral += 1
    return iteral,n
def modpow(a,n):#二乗
    if n==0:
        return 1
    elif n==1:
        return a%mod
    elif n%2==0:
        return (modpow(a,n/2)**2)%mod
    else:
        return (a*modpow(a,n-1))%mod
def modfact(l,r):#階乗
    fact=1
    for i in range(l-r+1):
        fact=fact*(r+i)%mod
    return fact
def comb(n,x):#組み合わせ
    S=modfact(n,n-x+1)
    fact=modfact(x,1)
    T=modpow(fact,mod-2)
    return S*T%mod

def sieve(N):#エラトステネスの篩
    prime = [0]*(N+1)
    isprime = [True]*(N+1)
    isprime[0]=isprime[1] = False
    num = 0
    for p in range(2,N+1):
        if isprime[p]:
            prime[num] = p
            num += 1
            for j in range(2*p,N+1,p):
                isprime[j] = False
    prime.sort()
    prime.reverse()
    for k in range(N-1):
        if prime[k+1] == 0:
            end = k
            break
    return prime[:end+1]
def main():
    N,M = map(int,input().split())
    b = {}
    for i in reversed(sieve(int(M**0.5)+10)):
        if M%i==0:
            num,M = prime(M,i)
            b[i] = num
    if M > 1:
        b[M] = 1
    ans = 1
    for num in b:
        ans *= comb(b[num]+N-1,b[num])
        ans %= mod
    print(ans)

if __name__ == "__main__":
    main()
