from collections import Counter


def main():
    """
    Aの空でない連続する部分列であって、
    その総和が 0になるものの個数を求めてください。
    ただし、ここで数えるのは 部分列の取り出し方 であることに注意してください。
    つまり、ある2つの部分列が列として同じでも、
    取り出した位置が異なるならば、それらは別々に数えるものとします。

    制約
        1 ≤ N ≤ 2×10^5
        −10^9 ≤ Ai ≤ 10^9
    """
    N = int(input())
    *A, = map(int, input().split())

    # f2(N, A)
    editorial(N, A)


def editorial(N, A):
    """
    部分列の和が0: 累積和の両端が同じ数であること
    """
    s = [0]
    for i in range(N):
        s.append(A[i] + s[-1])

    def ncr(n, r):
        if n < r:
            return 0
        from math import factorial as f
        # rまでの並べ方について,組合せなので1/r
        return f(n) // f(n - r) // f(r)

    c = Counter(s)
    ans = 0
    for v in c.values():
        ans += ncr(v, 2)

    print(ans)


if __name__ == '__main__':
    main()
