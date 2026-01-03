from collections import Counter

M = 10 ** 9 + 7

def main():
    n = int(input())
    a = [int(s) for s in input().split()]
    print(solve(a, n))

def solve(a, n):
    counter = Counter(a)

    if n % 2 == 0:
        for i in range(1, n, 2):
            if counter.get(i, None) != 2:
                return 0
    else:
        if counter.get(0, None) != 1:
            return 0
        for i in range(2, n, 2):
            if counter.get(i, None) != 2:
                return 0

    return modpow(2, n // 2, M)

def modpow(a, b, m):
    r = 1

    while b != 0:
        if b & 0x01:
            r = (r * a) % m
        a = (a * a) % m
        b >>= 1

    return r

main()
