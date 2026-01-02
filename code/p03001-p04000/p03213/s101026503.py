def is_prime(n):
    d = n - 1
    d = d // (d & -d)
    L = [2, 7, 61] if n < 1 << 32 else [2, 3, 5, 7, 11, 13, 17] if n < 1 << 48 else [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for a in L:
        t = d
        y = pow(a, t, n)
        if y == 1:
            continue
        while y != n - 1:
            y = y * y % n
            if y == 1 or t == n - 1: return 0
            t <<= 1
    return 1


def prime_factor(n):
    if n == 1:
        return {1: 1}

    pf = dict()
    r = list(range(2, n + 1))

    while n != 1:
        x = r[0]
        cnt = 0
        while n % x == 0:
            n = n // x
            cnt += 1
        if cnt > 0:
            pf[x] = cnt
        r = list(filter(lambda y: y % x != 0, r))

    return pf


def main():
    from collections import defaultdict
    n = int(input())
    d = defaultdict(int)
    for i in range(1, n + 1):
        p = prime_factor(i)
        for k, v in p.items():
            d[k] += v
    
    f2_, f4_, f14_, f24_, f74_ = 0, 0, 0, 0, 0
    for i in d.values():
        if i >= 2:
            f2_ += 1
        if i >= 4:
            f4_ += 1
        if i >= 14:
            f14_ += 1
        if i >= 24:
            f24_ += 1
        if i >= 74:
            f74_ += 1

    ans = f74_ + f24_ * (f2_ - 1) + f14_ * (f4_ - 1) + f4_ * (f4_ - 1) * (f2_ - 2) // 2
    print(ans)


if __name__ == '__main__':
    main()
