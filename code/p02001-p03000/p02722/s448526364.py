import sys
input = sys.stdin.readline


def inpl():
    return list(map(int, input().split()))


def factor(n):
    ret = {}
    p = 2
    root_n = int(n**0.5)
    while n > 1:
        if n % p == 0:
            n //= p
            ret[p] = ret.get(p, 0) + 1
        elif p <= root_n:
            p += 1
        else:
            p = n
    return ret


def gcd(a, b):
    # greatest common divisor
    while b > 0:
        a, b = b, a % b

    return a


def backtrack(pn_list, k=1):
    if (not pn_list) and k != 1 and k != N:
        factor_N.append(k)
    elif pn_list:
        # print(pn_list, k)
        p, v = pn_list[0]
        pn_list = pn_list[1:]
        # print(pn_list)
        for i in range(v + 1):
            backtrack(pn_list, k * (p**i))


def check(k):
    t = N
    while t % k == 0:
        t //= k
    return t % k == 1


factor_N = []


def solve():
    pn = factor(N)
    ans = 0
    a = 1
    for v in pn.values():
        a = gcd(a, v)
    for v in factor(a).values():
        a *= v + 1
    ans += a

    a = 1
    for v in factor(N - 1).values():
        a *= v + 1
    ans += a - 1

    pn_list = list(pn.items())
    # print(pn_list)
    backtrack(pn_list)
    for k in factor_N:
        if check(k):
            ans += 1

    return ans


N = int(input())

print(solve())
