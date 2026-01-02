def main():
    """
    """
    N, M, Q = map(int, input().split())
    L, R = zip(*(
        map(int, input().split())
        for _ in range(M)
    ))
    p, q = zip(*(
        map(int, input().split())
        for _ in range(Q)
    ))

    # answers = f(N, M, Q, L, R, p, q)
    # experiment(N, M, Q, L, R, p, q)
    # answers = TLE(N, M, Q, L, R, p, q)
    answers = editorial(N, M, Q, L, R, p, q)
    for ans in answers:
        print(ans)


def editorial(N, M, Q, L, R, p, q):
    """
    ２次元累積和のライブラリを持っておくとよいらしい
        確かに実装ミスりそう

    """
    # LRの組合せ, N<=500より間に合う
    t1 = [[0] * (N+1) for _ in range(N+1)]
    t2 = [[0] * (N+1) for _ in range(N+1)]
    for l, r in zip(L, R):
        t1[l][r] += 1

    # Lごとの累積和
    for l in range(1, N+1):
        for r in range(1, N+1):
            t2[l][r] = t2[l][r-1] + t1[l][r]

    answers = []
    for _p, _q in zip(p, q):
        ans = 0
        for l in range(_p, _q+1):
            ans += t2[l][_q] - t2[l][_p-1]

        answers.append(ans)

    return answers


def TLE(N, M, Q, L, R, p, q):
    """
    10^5 * 10^5
    """
    answers = []
    for _p, _q in zip(p, q):
        ans = 0
        for left, right in zip(L, R):
            if _p <= left and right <= _q:
                ans += 1

        answers.append(ans)

    return answers


if __name__ == '__main__':
    main()
