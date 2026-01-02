N, M = map(int, input().split())
MOD = 10**9 + 7

def primeFact(N):
    R = int(N**(0.5)) + 1  # 素数の範囲
    factor = {}  # 素数のリスト
    n = N
    for num in range(2, R):
        factor[num] = 0
        while n % num == 0:
            n //= num
            factor[num] += 1
    if n > 1 :
        factor[n] = 1
    return factor

def dictFilter (filter, dic) :
    return { key : val for key, val in dic.items() if filter(key, val)}

primeCount = dictFilter(lambda key, val : val > 0, primeFact(M))

def comb(n, k) :
    p = 1
    div = 1
    for i in range(k) :
        p *= (n - i)
        div *= (i + 1)
    return p // div

ans = 1
for _, count in primeCount.items() :
    ans *= comb(count + N - 1, count) % MOD

print(ans % MOD)