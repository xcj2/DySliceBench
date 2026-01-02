def binaryarray_to_int(a):
    res = 0
    for x in a:
        res = (res << 1) + x
    return res

def count_bits(x):
    res = 0
    while x > 0:
        res += (x & 1)
        x = x >> 1
    return res


def solve():
    N = int(input())

    F = [
        binaryarray_to_int(
            [int(x) for x in input().split()]
        )
        for _ in range(N)
    ]

    P = [
        [int(x) for x in input().split()]
        for _ in range(N)
    ]

    # simulate all patterns
    ans = -float("inf")
    for mask in range(1, 1024):
        p = 0
        for i in range(N):
            bit = mask & F[i]
            c = count_bits(bit)
            p += P[i][c]
        ans = max(ans, p)

    return ans


print(solve())