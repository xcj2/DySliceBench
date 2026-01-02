import itertools
import collections


def prime_factor_table(n):
    table = [0] * (n + 1)

    for i in range(2, n + 1):
        if table[i] == 0:
            for j in range(i + i, n + 1, i):
                table[j] = i

    return table


def prime_factor(n, prime_factor_table):
    prime_count = collections.Counter()

    while prime_factor_table[n] != 0:
        prime_count[prime_factor_table[n]] += 1
        n //= prime_factor_table[n]
    prime_count[n] += 1

    return prime_count


def solve(N):
    ans = 1

    table = prime_factor_table(1000000)

    for i in range(2, N):
        tmp = prime_factor(i, table)
        tt = 1
        for t in tmp:
            tt *= (tmp[t]+1)
        ans += tt
    return ans


if __name__ == "__main__":
    N = int(input())
    print(solve(N))
