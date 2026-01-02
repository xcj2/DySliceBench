import math
from functools import reduce


def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


def lcm(numbers):
    return reduce(lcm_base, numbers, 1)


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def commonDivisors(x1, x2):
    cf = []
    for i in range(2, min(x1, x2) + 1):
        if x1 % i == 0 and x2 % i == 0:
            cf.append(i)
    return cf


def solve():
    N, M = [int(x) for x in input().split()]
    S = input()
    T = input()
    # cdivs = commonDivisors(N, M)
    # ans_flag = True
    # print(cdivs)
    # for c in cdivs:
    #     if S[c - 1] != T[c - 1]:
    #         ans_flag = False
    # if ans_flag:
    #     print(lcm([N, M]))
    # else:
    #     print(-1)
    # N_divs = make_divisors(N)
    # M_divs = make_divisors(M)
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
    # print(N_divs, M_divs)
    # return
    # ans_flag = True
    # for d in divs:
    #     if S[d] != T[d]:
    #         ans_flag = False
    # if ans_flag:
    #     print(lcm([N, M]))
    # else:
    #     print(-1)


if __name__ == '__main__':
    solve()
