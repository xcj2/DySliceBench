def get_primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return set([i for i in range(n + 1) if is_prime[i]])


def solve():
    # A = [int(n) for n in input().split()]

    NMAX = 100000
    primes = set(get_primes(NMAX+1))
    table = [0] * NMAX

    for n in range(1, NMAX):
        table[n] = table[n-1] + int(n in primes and (n+1)//2 in primes)

    Q = int(input())
    for _ in range(Q):
        l, r = [int(x) for x in input().split()]
        print(table[r]-table[l-1])
    
    return 0


def main():
    solve()


if __name__ == '__main__':
    main()
