#!/usr/bin/env pypy3


M = 10 ** 9 + 7


def naive_inv_num(xs):
    n = len(xs)
    res = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if xs[i] > xs[j]:
                res += 1
    return res


def rep_inv_num(k, xs, mod=M):
    c1 = naive_inv_num(xs)
    c2 = naive_inv_num(xs * 2)
    c3 = naive_inv_num(xs * 3)
    d1 = c2 - c1
    f = c3 - 2 * c2 + c1
    res = c1
    res += (k - 1) * d1
    res %= mod
    res += f * (k - 1) * k // 2
    res %= mod
    res -= f * (k - 1)
    res %= mod
    return res


def main():
    _, k = (int(z) for z in input().split())
    xs = [int(x) for x in input().split()]
    res = rep_inv_num(k, xs)
    print(res)


if __name__ == "__main__":
    main()
