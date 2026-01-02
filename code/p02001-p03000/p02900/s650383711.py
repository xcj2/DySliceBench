import math

def primelist(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

def factorization(n):
    plist = primelist(int(n**0.5))
    factor = []
    for p in plist:
        k = 0
        while n%p==0:
            k+=1
            n//=p
        if k>0:
            factor.append((p,k))
        if n==1:
            break
    if n!=1:
        factor.append((n,1))

    return factor

def divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


def main():
    a,b = tuple(map(int,input().split()))

    g = math.gcd(a,b)
    factors = factorization(g)
    print(len(factors)+1)

if __name__ == "__main__":
    main()
