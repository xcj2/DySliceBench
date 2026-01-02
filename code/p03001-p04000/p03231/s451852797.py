import math
from functools import reduce


def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


def lcm(numbers):
    return reduce(lcm_base, numbers, 1)


def solve():
    N, M = [int(x) for x in input().split()]
    S = input()
    T = input()

    L = lcm([N, M])
    ic, jc = 0, 0
    i, j = ic * L // N + 1, jc * L // M + 1
    ans = L
    while ic < N and jc < M:
        # print(i, j, ic, jc, S[ic], S[jc])
        if i == j:
            if S[ic] != T[jc]:
                ans = '-1'
                break
            ic += 1
            jc += 1
            i = ic * L // N + 1
            j = jc * L // M + 1
        elif i < j:
            ic += 1
            i = ic * L // N + 1
        elif i > j:
            jc += 1
            j = jc * L // M + 1
    print(ans)


if __name__ == '__main__':
    solve()
