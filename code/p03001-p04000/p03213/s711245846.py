import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
INF = 10 ** 18
MOD = 10 ** 9 + 7

def get_primes_tuple(n):  # including n
    isPrime = [True for _ in range(n+1)]
    isPrime[0] = False
    isPrime[1] = False
    for j in range(4, n+1, 2): isPrime[j] = False  # multiples of 2
    primes = [2]

    for i in range(3, int(n**0.5)+1):
        if not isPrime[i]: continue
        primes.append(i)
        for j in range(i*i, n+1, i+i):  # j = (i*i, (i+2)*i, ..., m*i <= n)
            isPrime[j] = False
    # return tuple(isPrime)
    return tuple(primes)


primes = get_primes_tuple(10000)
def prime_factorization(n):
    pf = []
    for p in primes:
        while n != 1 and n%p == 0:
            pf.append(p)
            n //= p
    return pf


import collections

def main(): 
    n = II()

    pf_of_n_factorial = collections.defaultdict(int)
    for i in range(2, n+1):
        for p in prime_factorization(i):
            pf_of_n_factorial[p] += 1

    import itertools

    ans = 0

    # 1つの素数が75-1個以上ある。
    for i in primes:
        if pf_of_n_factorial[i] >= 74:
            ans += 1

    # 3-1, 25-1 または 5-1, 15-1
    for i, j in itertools.permutations(primes, 2):
        if pf_of_n_factorial[i] >= 2 and pf_of_n_factorial[j] >= 24:
            ans += 1
        if pf_of_n_factorial[i] >= 4 and pf_of_n_factorial[j] >= 14:
            ans += 1

    # 3-1, 5-1, 5-1
    for i, j, k in itertools.permutations(primes, 3):
        if pf_of_n_factorial[i] >= 2 and pf_of_n_factorial[j] >= 4 and pf_of_n_factorial[k] >= 4 and j<k:
            ans += 1

    print(ans)


main()