def fact(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x


def nCr(n, r):
    return fact(n) // (fact(n - r) * fact(r))


def solve(N, K):
    if N < int("1" * K):
        return 0
    digits = [int(c) for c in str(N)]
    places = len(digits)
    count = 0
    for i in range(K - 1, places):
        # first digit then choose K-1 more places each 1-9
        firstChoice = 9
        if i == places - 1:
            # handle digits[0] case separate
            firstChoice = digits[0] - 1
        count += firstChoice * (9 ** (K - 1)) * nCr(i, K - 1)
    # digits[0] case
    if K == 1:
        count += 1
    else:
        count += solve(int("".join(map(str, digits[1:]))), K - 1)
    return count


N, = list(map(int, input().split()))
K, = list(map(int, input().split()))

print(solve(N, K))
