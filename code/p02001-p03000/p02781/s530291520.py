from math import factorial

N = int(input())
K = int(input())


def ncr(n, r):
    if n < r:
        return 0
    return factorial(n) // factorial(r) // factorial(n - r)


def k1(n):
    s = str(n)
    return (len(s) - 1) * 9 + int(s[0])


def k2(n):
    if n < 10:
        return 0
    s = str(n)
    res = ncr(len(s)-1, 2) * 9 * 9
    res += (int(s[0]) - 1) * k1(10 ** (len(s) - 1) - 1) + k1(int(s[1:]))
    return res


def k3(n):
    s = str(n)
    res = ncr(len(s)-1, 3)*9*9*9
    res += (int(s[0]) - 1) * k2(10 ** (len(s) - 1) - 1) + k2(int(s[1:]))
    return res


kf = [k1, k2, k3]
print(kf[K-1](N))
