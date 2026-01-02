def main():
    N, K = map(int, input().split())

    # TLE(N, K)
    editorial(N, K)


def editorial(N, K):
    """
    # https://twitter.com/tanakh/status/972832191863336960
    N = p*b + r (0 <= r < b)

    a固定: bが変わるので余りが変わるため意味なし
    b固定: aが変わっても余りは一定周期になる
        0%b, 1%b, 2%b, ..., (b-1)%b, b%b, (b+1)%b, ..., (pb-1)%b, pb%b, ..., (pb+r)%b
        0,   1,   2,   ..., (b-1),   0,   1,       ...,  b-1,      0,    ..., r
        余りの数列: (0...b-1)がp個 と 0...r
        ↓
        0...K-1, K...b-1
        b個の中にKより小さい数はK個
        よって, b - min(b, K) = max(b-K, 0)
    """
    ans = 0
    if K == 0:
        # 次のfor loop計算を0込みにせず、
        # 余り>=0つまりa*bのすべての組合せ数N*Nを返して終了でも良い
        ans -= N

    # 余り>=Kのため mod K+1から
    # K=0のとき、1-N loopよりN余分
    for b in range(K+1, N+1):
        # 0-Nまでの0込みのためN+1
        p, r = divmod(N+1, b)

        ans += p * (b - K) + max(0, r - K)

    print(ans)


def TLE(N, K):
    """
    1 <= a,b <= N <= 10^5
    a mod b >= K
    0 <= K <= N-1
    """
    # a < b: mod b = a, K <= a <= N
    ans = 0
    for a in range(K, N):
        b_pattern = N - a
        ans += b_pattern

    # a > b: mod b = x
    # K >= b: mod b = 0 or K< より
    # K < b < a <= N
    for a in range(K+2, N+1):
        for b in range(K+1, a):
            if a % b >= K:
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
