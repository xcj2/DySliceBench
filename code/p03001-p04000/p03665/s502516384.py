def main():
    N, P = map(int, input().split())
    *A, = map(int, input().split())

    odd = sum(a % 2 for a in A)
    even = N - odd
    o, e = 0, 0
    # 奇数枚の袋の選び方
    # P=0: 奇数個含まれる袋から足して２の倍数になる袋の組合せ(袋0でもよい)
    # P=1: 奇数なので奇数枚の袋を奇数個
    for i in range(P, odd+1, 2):
        o += ncr(odd, i)

    for i in range(even+1):
        e += ncr(even, i)
    ans = o * e

    print(ans)


def _factorial(n):
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    a = 1
    for i in range(1, n + 1):
        a *= i
    return a


def npr(n, r):
    if n < r:
        return 0
    a = 1
    for i in range(r):
        a *= n - i
    return a


def ncr(n, r):
    _npr = npr(n, r)
    if _npr == 0:
        return 0
    return _npr // _factorial(r)


if __name__ == '__main__':
    main()
