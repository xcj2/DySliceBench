import functools
import fractions
MOD = 10**9+7


def sieve(n):
    result = [0] * (n+1)
    result[0] = result[1] = -1
    #primes = []
    for i in range(2, n+1):
        if(result[i]):
            continue
        # primes.append(i)
        result[i] = i
        for j in range(i*i, n+1, i):
            if not result[j]:
                result[j] = i
    return result


def is_prime(table, x):
    return table[x] == x


def factor(table, x):
    result = {}
    while(x != 1):
        p = str(table[x])
        if p not in result:
            result[p] = 1
        else:
            result[p] += 1
        x //= int(p)
    return result


def main():
    n = int(input())
    x = list(map(int, input().split()))

    table = sieve(10**6)
    max_table = {}
    for i in range(n):
        f = factor(table, x[i])
        for j in f:
            if j not in max_table:
                max_table[j] = f[j]
            else:
                max_table[j] = max(max_table[j], f[j])

    lcm = 1
    for p in max_table:
        lcm *= int(p)**max_table[p] % MOD

    ans = 0
    for i in range(n):
        ans += lcm//x[i]
    print(ans % MOD)


main()
