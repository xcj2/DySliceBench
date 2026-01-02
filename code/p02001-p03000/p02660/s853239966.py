import math
def solve():
    N = int(input())
    divisors = calc_divisors(N)
    divisors.sort()

    now = N
    i = 1
    ans = 0
    while i != len(divisors):
        if isPrime(divisors[i]) and now % divisors[i] == 0:
            now /= divisors[i]
            ans += 1
        else:
            if len(set(prime_factorize(divisors[i]))) == 1 and now % divisors[i] == 0:
                now /= divisors[i]
                ans += 1
        i += 1
    
    print(ans)

def isPrime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

def sieve(n):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False

    p = 0
    for i in range(2,n+1):
        if is_prime[i]:
            p = i
            for j in range(p+p, n+1, p):
                is_prime[j] = False
        
        if p * p > n:
            break
    
    primes = []
    for i in range(2,n+1):
        if is_prime[i]:
            primes.append(i)

    return primes

def prime_factorize(n):
    prime_numbers = []
    for p in range(2, int(math.sqrt(n)+1)):
        if n % p != 0:
            continue
        while n % p == 0:
            n /= p
            prime_numbers.append(p)

    if n != 1:
        prime_numbers.append(n)
    return prime_numbers

def calc_divisors(n):
    divisors = []
    for i in range(1,int(math.sqrt(n)+1)):
        if n % i == 0:
            divisors.append(i)
            if (i*i != n):
                divisors.append(n//i)

    return divisors
if __name__ == '__main__':
    solve()