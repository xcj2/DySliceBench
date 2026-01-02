# https://atcoder.jp/contests/abc150/submissions/9395610

def main():
    from functools import reduce

    def count_two(x):
        ret = 0
        while x % 2 == 0:
            x //= 2
            ret += 1
        return ret

    def lcm(a, b):
        def _gcd(a, b):
            return a if b == 0 else _gcd(b, a % b)

        return a * b // _gcd(a, b)

    n, m = map(int, input().split())
    *a, = map(int, input().split())

    a = [x >> 1 for x in a]

    e = len(set(map(count_two, a)))
    if e != 1:
        print(0)
        return

    # x=(ai/2)*(2p+1)と変形する
    # 2p+1は奇数だから、
    # すべてのiについて,xと(ai/2)は,2で割れる回数が等しい必要がある

    x = reduce(lcm, a)
    ret = (m // x) - (m // (x + x))
    print(ret)
    # xは(ai/2)の最小公倍数の奇数倍
    # (ai/2)の最小公倍数の倍数全体から
    # (ai/2)の最小公倍数の偶数倍を引いた残り


if __name__ == '__main__':
    main()
