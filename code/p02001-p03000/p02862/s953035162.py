INF = float("inf") #const
MOD = 10**9+7 #const
MAX = 510000 #const

def repeat(n,p):
    if p == 0:
        return 1
    if p%2==0:
        t = repeat(n,p//2)
        return t * t % MOD
    return n * repeat(n,p-1) % MOD


def com(n,r):
    if n < r or n < 0:
        return 0
    if n == 0 and r == 0:
        return 1
    fact = [0] * (10**6+1)
    fact[0] = 1
    for i in range(n):
        fact[i+1] = fact[i] * (i+1) % MOD #階乗計算
    f_inv = repeat(fact[r],MOD-2)
    f = repeat(fact[n-r],MOD-2)
    return fact[n] * f_inv * f % MOD


def main():
    x,y = map(int,input().split())
    if (x+y)%3 != 0:
        print(0)
        return
    n = (2*y - x)//3
    m = (2*x - y)//3
    print(com(n+m,n))


if __name__ == "__main__":
    main()
