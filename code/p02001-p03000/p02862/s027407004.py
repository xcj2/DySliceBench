#  --*-coding:utf-8-*--

MOD = 10**9 + 7

def modPow(a, b, mod):
    x = 1
    
    while b > 0:
        if b & 1:
            x = (x*a)%mod

        a = (a**2)%mod
        b //= 2

    return x

def modFact(n, mod):
    x = 1

    for i in range(2, n+1):
        x = x*i%mod

    return x


def getModInv(a, b):
    return 1 if (a == 1) else int((1-b*getModInv(b%a, a))/a%b)


def f(X, Y):
    if X*2<Y or Y*2<X or (X+Y)%3 != 0:
        return 0

    N = (X+Y)//3
    K = X - N

    return(modFact(N, MOD)*(getModInv(
        modFact(K, MOD)*modFact(N-K, MOD)%MOD, MOD))%MOD)



def main():
    X, Y = map(int, input().split())
    print(f(X, Y))


if __name__ == '__main__':
    main()
