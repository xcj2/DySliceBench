# D - 756
# 75 = 3*5*5なので、(4個以上ある素因数のうち2つを選ぶ組合せ)×(残りから2個以上ある素因数1つを選ぶ組合せ) が解の一部
# 15*5, 25*3, 75についても同様

import collections, math

N = int(input())

# n以下の全ての素数のセットを返す関数
def prime_set(n):
    primes = set(range(2, n+1))
    for i in range(2, int(n**0.5) + 1):
        primes.difference_update(range(i*2, n+1, i))
    return primes

# nを素因数分解して素因数の全リストを返す関数
def prime_factors_duplicating_list(n):
    f = []
    for i in prime_set(int(n**0.5) + 1):
        while n % i == 0:
            f.append(i)
            n //= i
    if n > 1:
        f.append(n)
    return f

def comb(n, r):
    if n < r:
        return 0
    else:
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N_factorial_prime_factors = []
for i in range(1, N+1):
    N_factorial_prime_factors.extend(prime_factors_duplicating_list(i))

N_factorial_prime_factors = collections.Counter(N_factorial_prime_factors)

n_74plus_factors = set()
n_24plus_factors = set()
n_14plus_factors = set()
n_4plus_factors = set()
n_2plus_factors = set()

for key in N_factorial_prime_factors:
    for border in [2,4,14,24,74]:
        if N_factorial_prime_factors[key] >= border:
            eval("n_" + str(border) + "plus_factors.add(key)")

ans = 0
ans += comb(len(n_4plus_factors), 2) * (len(n_4plus_factors) - 2 + len(n_2plus_factors - n_4plus_factors)) # 3*5*5
ans += len(n_14plus_factors) * (len(n_14plus_factors) - 1 + len(n_4plus_factors - n_14plus_factors)) # 15*5
ans += len(n_24plus_factors) * (len(n_24plus_factors) - 1 + len(n_2plus_factors - n_24plus_factors)) # 25*3
ans += len(n_74plus_factors) # 75

print(ans)