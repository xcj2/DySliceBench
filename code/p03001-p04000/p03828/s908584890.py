import sys
def input(): return sys.stdin.readline().strip()
mod = 10**9+7


def get_sieve_of_eratosthenes(n):
    """
    エラトステネスの篩。√N以下の数に対して2から順にその数の倍数を消していく。
    計算量は「調和級数」になるのがミソ。具体的には
        N/2 + N/3 + N/5 + ... + N/(√N) = N * (1/2 + 1/3 + 1/5 + ... + 1/√N)
                                       = N * loglog(√N) (素数の逆数和の発散スピードがこれ)
                                       = N(loglogN - log2)
    """
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        return [0] * (n + 1)
    prime = [1] * (n + 1)
    prime[0] = prime[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if not prime[i]: continue
        for j in range(i * 2, n + 1, i):
            prime[j] = 0
    return prime


def main():
    n = int(input())
    primes = get_sieve_of_eratosthenes(n)
    ans = 1
    for p in range(2, n + 1):
        if primes[p] == 0: continue
        cur = p
        num = 0
        while cur <= n:
            num += n // cur
            cur *= p
        ans *= (num + 1)
        ans %= mod
    print(ans)


if __name__ == "__main__":
    main()
