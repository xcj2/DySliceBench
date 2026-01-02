import math


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    """
    """
    N = read_int()
    A = read_ints()
    prefix = [-1]*N
    # prefix[i] is gcd of numbers 0..i-2
    suffix = [-1]*N
    for i in range(N-1):
        if i == 0:
            prefix[i+1] = A[i]
        else:
            prefix[i+1] = math.gcd(prefix[i], A[i])
    for i in range(N-1, 0, -1):
        if i == N-1:
            suffix[i-1] = A[i]
        else:
            suffix[i-1] = math.gcd(suffix[i], A[i])

    max_gcd = -1
    for i in range(N):
        gcd = -1
        if prefix[i] != -1 and suffix[i] != -1:
            gcd = math.gcd(prefix[i], suffix[i])
        elif prefix[i] == -1:
            gcd = suffix[i]
        else:
            gcd = prefix[i]
        max_gcd = max(max_gcd, gcd)
    return max_gcd


if __name__ == '__main__':
    print(solve())
