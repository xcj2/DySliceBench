import sys
import collections

sys.setrecursionlimit(10**6)
MOD = pow(10,9)+7

def kaijo(n):
    if n <= 1:
        return 1
    else:
        return n * kaijo(n-1)

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

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

def main():
    N = int(input())
    if N == 1:
        print(1)
        return
    counter = collections.Counter([])
    for n in range(N, 0, -1):
        counter += collections.Counter(prime_factorize(n))
    items = list(zip(*counter.items()))
    ans = 1
    for i in items[1]:
        ans *= i+1
        ans %= MOD
    print(ans)

    #n = kaijo(N)
    #print(n)
    #m = make_divisors(n)
    ##m.sort()
    #print(m)
    #print(len(m)%MOD)

if __name__ == "__main__":
    main()
