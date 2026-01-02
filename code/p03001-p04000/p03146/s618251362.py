def main():
    s = int(input())

    ans = solve(s)
    print(ans)


def solve(s):
    """
    数列 a={a1,a2,a3,......} は、以下のようにして定まります。
    初項 s は入力で与えられる。

    関数 f(n) を以下のように定める
    n が偶数なら f(n)=n/2
    n が奇数なら f(n)=3n+1

    i=1 のとき ai=s
    i>1 のとき ai=f(a(i−1))

    このとき、次の条件を満たす最小の整数 mを求めてください。
    a(m) = a(n) (m>n) を満たす整数 n が存在する。
    制約: 1 ≦ s ≦ 100
    入力はすべて整数である。
    a のすべての要素、および条件を満たす最小の m は 1000000 以下となることが保証される。
    """
    bef_a = s
    d = {s: None}

    def f(n):
        if n % 2 == 0:
            return n // 2
        else:
            return 3 * n + 1

    for i in range(2, 1000000 + 1):
        bef_a = f(bef_a)
        if bef_a in d:
            return i

        d[bef_a] = None


if __name__ == '__main__':
    main()
