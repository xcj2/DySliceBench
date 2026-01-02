import sys
import collections
def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def TI(): return tuple(map(int,input().split()))
def RN(N): return [input().strip() for i in range(N)]

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def main():
    N = II()
    n = N
    ans = 0

    if N == 0 or N == 1:
        print(0)

    else:
        numl = prime_factorize(N)
        j = len(set(numl))
        setl = list(set(numl))
        c = collections.Counter(numl)

        for i in setl:
            #print(i,c[i])
            k = 1
            ci = c[i]
            while True:
                if ci-k>=0:
                    ans += 1
                else:
                    break
                ci = ci-k
                k += 1


        print(ans)

        """
        for i in range(2,N+1):
            if n % i == 0:
                n = n/i
                ans += 1
            if n == 1:
                break
        print(ans)
        """

    


if __name__ == "__main__":
	main()