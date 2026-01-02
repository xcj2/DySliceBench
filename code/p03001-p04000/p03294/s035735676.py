def main():
    """
    2 <=  N <= 10^3
    2 <= ai <= 10^5

    非負整数 m に対して
    f(m) = (m mod a1) + (m mod a2) + (m mod aN)
    f_max

    mの制約は問題文中には直接記述されていない
    """
    N = int(input())
    *A, = map(int, input().split())

    ans = f(N, A)
    print(ans)


def f(N, A):
    """
    直感: 最小公倍数,最大公約数
        最小公倍数のm ならすべてのaで割り切れる
        つまり最小公倍数-1 ならすべてのaについて m mod ai = ai - 1

    m=a_MAX-1, (m mod a_MAX) が最大
    ただし他のa=a_MAX-1 の場合、f(m)は小さくなってしまう
    aiに対して1 <= m <= a_Max-1 をすべて試す: 10^5 * 3 * 10^3 => TLE
    """
    try:
        # py3.5
        from math import gcd
    except:
        from fractions import gcd

    def lcm(x, y):
        return x * y // gcd(x, y)

    m1 = lcm(A[0], A[1])
    for a in A[2:]:
        m1 = lcm(m1, a)

    m = m1 - 1
    ans = sum(m % a for a in A)

    return ans


def WA(N, A):
    ans = 0
    m_max = max(A) * 2 - 1
    for m in range(1, m_max):
        mods = [m % a for a in A]
        tmp = sum(mods)
        print(*(mods + [tmp]), sep="\t")
        ans = max(ans, tmp)

    return ans


if __name__ == '__main__':
    main()
