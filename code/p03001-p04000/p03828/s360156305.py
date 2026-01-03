def primes_eratosthenes(n:int) -> list:
    isprime = [True] * (n+1)
    isprime[0] = isprime[1] = False

    for i in range(2, n+1):
        if isprime[i]:
            j = i + i
            while j <= n:
                isprime[j] = False
                j += i
    return [i for i in range(2,n+1) if isprime[i]]


def add_factor(d: dict, n: int, primes: list) -> dict:
    for p in primes:
        while n%p == 0:
            n /= p
            d[p] = d.get(p, 0) + 1
        if n==1:
            break
    return d 


def solve(n):
    primes = primes_eratosthenes(n)

    d = {}

    for i in range(2,n+1):
        d = add_factor(d, i, primes)

    MOD = 10**9 + 7
    ans = 1
    for v in d.values():
        ans = ans * (v+1) % MOD
    
    return ans
    

def main():
    n = int(input())
    ans = solve(n)
    print(ans)


main()
