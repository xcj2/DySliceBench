def main():
    import math
    from collections import Counter

    N,M = map(int,input().split())
    a = []
    def prime_factorize(n):
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
    prime_factorize(M)
    def combinations_count(n, r):
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
    divisors = Counter(a)
    count = 1
    for k,v in divisors.items():
        count *= combinations_count(v+N-1,v)

    print(count%(10**9+7))
main()