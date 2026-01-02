import sys

MOD = 10 ** 9 + 7

def main():
    n, m = [int(s) for s in input().split()]
    print(solve(m, n))

def solve(m, n):
    factors = list(get_prime_factors(m))
    h = max((c for f, c in factors), default=0)

    table = dict()
    table[1] = [1 for _ in range(h + 1)]

    i = 1
    while i < n:
        j = n & (i - 1)
        table[i * 2] = [0 for _ in range(h + 1)]
        if n & i != 0 and j != 0:
            table[i + j] = [0 for _ in range(h + 1)]
        for x in range(h + 1):
            for y in range(h + 1 - x):
                table[i * 2][x + y] = (table[i * 2][x + y] + table[i][x] * table[i][y]) % MOD
                if n & i != 0 and j != 0:
                    table[i + j][x + y] = (table[i + j][x + y] + table[i][x] * table[j][y]) % MOD

        if n & i == 0:
            del table[i]
        if n & i != 0 and j != 0:
            del table[i]
            del table[j]

        i *= 2

    ans = 1
    for f, c in factors:
        ans = ans * table[n][c] % MOD
    return ans

def get_prime_factors(n):
    import itertools

    m = n
    for i in itertools.count(2):
        if i * i > m:
            break

        c = 0
        while True:
            x, y = divmod(m, i)
            if y != 0:
                break
            c += 1
            m = x
        if c != 0:
            yield i, c

    if m != 1:
        yield m, 1


main()
