import sys
from collections import Counter

read = sys.stdin.read


# 最小素因数を求める（エラトステネスの篩の亜種？）
def min_factor(n):
    sieve = list(range(n + 1))
    sieve[2::2] = [2] * (n // 2)

    # エラトステネスのふるい
    def sieve_of_eratosthenes(n):
        sieve = [True] * n
        for i in range(3, int(n ** 0.5) + 1, 2):
            if sieve[i]:
                sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
        return [i for i in range(3, n, 2) if sieve[i]]

    for i in sieve_of_eratosthenes(int(n ** 0.5) + 2):
        if sieve[i] == i:
            sieve[i * i::2 * i] = [i] * ((n - i * i - 1) // (2 * i) + 1)
    return sieve


# 素因数分解
def prime_factorize(n):
    a = [1]
    while n != 1:
        b = table[n]
        a.append(b)
        n //= b
    return a


N, *A = map(int, read().split())
mod = 10 ** 9 + 7

table = min_factor(10 ** 6)
dic = {}

for i in A:
    for key, value in Counter(prime_factorize(i)).items():
        # print(key, value)
        if dic.get(key):
            if dic[key] < value:
                dic[key] = value
        else:
            dic[key] = value

lcm = 1
for i, j in dic.items():
    lcm *= pow(i, j, mod)
    lcm %= mod

answer = sum(lcm * pow(i, mod - 2, mod) for i in A) % mod
print(answer)
