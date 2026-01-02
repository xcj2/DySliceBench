# ABC162c


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    # 最大公約数,最大公約数
    # from fractions import gcd
    from functools import reduce
    from math import gcd

    def lcm_base(a, b):
        return a * b // gcd(a, b)

    def lcm(*numbers):
        return reduce(lcm_base, numbers, 1)

    def gcds(*numbers):
        return reduce(gcd, numbers)

    k = int(input())
    ans = 0
    for i in range(1, k + 1):
        for j in range(1, k + 1):
            for l in range(1, k + 1):
                ans += gcds(i, j, l)
    print(ans)


if __name__ == '__main__':
    main()
