# coding: utf-8
from bisect import bisect_left, bisect_right
def eratosthenes(N):
    # 素数判定
    flag = True
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            flag = False
            break
    return flag

def make_prime_nums(N):
    # Nまでの素数のリストを作成
    prime_tf = [True for _ in range(N+1)]
    prime_tf[0] = False
    prime_tf[1] = False
    for i in range(N+1):
        if prime_tf[i]:
            if eratosthenes(i):
                for j in range(i*2, N+1, i):
                    prime_tf[j] = False
    primes = [i for i in range(N+1) if prime_tf[i]]
    return primes

def make_prime_new(L):
    new_primes = []
    for l in L:
        tmp = (l+1) // 2
        if eratosthenes(tmp):
            new_primes.append(l)
    return new_primes

primes = make_prime_nums(10**5)
primes = make_prime_new(primes)[1:]
# print(primes)
N = int(input())
for _ in range(N):
    l, r = map(int, input().split())
    r += 1
    l_idx = bisect_left(primes, l)
    r_idx = bisect_left(primes, r)
    if l == r and l_idx == r_idx and l == primes[l_idx]:
        print(1)
    else:
        print(r_idx - l_idx)
