#  --*-coding:utf-8-*--

MOD = 10**9 + 7

Factors = [0]*(10**5+1)
Factors[0] = 1
x = 1

for i in range(1, 10**5+1):
    x = x*i%MOD;
    Factors[i] = x

def getModInv(a, b):
    return 1 if (a == 1) else int((1-b*getModInv(b%a, a))/a%b)


def getComb(n, r):
    return (Factors[n]*
            getModInv(Factors[r], MOD)%MOD*
            getModInv(Factors[n-r], MOD)%MOD)



def main():
    N, K = map(int, input().split())
    A = sorted(map(int, input().split()))

    S = 0
    for i in range(N-K+1):
        c = getComb(N-1-i, K-1)
        S += (A[-i-1] - A[i])*c%MOD

    print(S%MOD)



        


if __name__ == '__main__':
    main()
