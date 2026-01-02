def main():
    """
    2 <= N <= 10^5
    1 <= M <= 10^5
    1 <= ai < bi <= N
    (ai, bi) != (aj, bj)
    """
    N, M = map(int, input().split())
    A, B = zip(*[
        map(int, input().split())
        for _ in range(M)
    ])
    # ans = WA(N, M, A, B)
    ans = editorial(N, M, A, B)
    # ans = TLE(N, M, A, B)

    print(ans)


def editorial(N, M, A, B):
    ans1 = AC_b_sort(N, M, A, B)
    ans2 = AC_a_sort(N, M, A, B)
    assert ans1 == ans2
    return ans1


def AC_b_sort(N, M, A, B):
    ab = sorted(zip(A, B), key=lambda x: (x[1], x[0]))
    ans = 0
    bef_b = 0
    for a, b in ab:
        # print(" " * (a-1), a, "-" * (b - a - 1), b, sep="")
        if bef_b <= a:
            ans += 1
            bef_b = b

    return ans


def AC_a_sort(N, M, A, B):
    ab = sorted(zip(A, B), key=lambda x: (x[0], -x[1]))
    ans = 0
    bef_b = float("inf")
    for a, b in ab:
        # print(" " * (a-1), a, "-" * (b - a - 1), b, sep="")
        if bef_b <= a:
            ans += 1
            bef_b = b
        else:
            bef_b = min(bef_b, b)

    return ans + 1


def TLE(N, M, A, B):
    """
    """
    ans = N - 1
    for a in A:
        for b in B:
            pass

    return ans


def WA(N, M, A, B):
    """
    ai, bi の分断:

    入力例1
        1, 4 の分断
            橋1-3 のどれかを除去
        2, 5 の分断
            橋2-4 のどれかを除去
        共通部: 2-3
        要望ごとの共通部を探す必要がある
            M^2: TLE

    A_min: 西
    A_max: 東
    B_min: 西
    B_max: 東

    入力例2
    9 5
    1------8
     2----7
      3-5
       4-6
          7-9

    a_min,b_max の順に並べる
    要望の東側が以前の西側未満ならOK
    要望の西側が以前の東側を超えないならOK ?
    """
    ab = sorted(zip(A, B), key=lambda x: (x[0], -x[1]))
    ans = 0
    bef_a, bef_b = -1, float("inf")
    for i, (a, b) in enumerate(ab):
        print(" " * (a-1), a, "-" * (b - a - 1), b, sep="")
        if bef_a <= a < b <= bef_b:
            pass
        elif bef_b <= a:
            ans += 1
        elif bef_a < a < bef_b < b:
            pass

        bef_a, bef_b = a, b

    return ans + 1


if __name__ == '__main__':
    main()
