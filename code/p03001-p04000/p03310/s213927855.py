from bisect import bisect_right


def main():
    """
    4 <= N <= 2 * 10^5
    1 <= Ai <= 10^9
    """
    N = int(input())
    *A, = map(int, input().split())

    ans = f(N, A)
    # ans = TLE(N, A)

    print(ans)


def test_ans():
    NA_ans = [
        (5, [3, 2, 4, 1, 2], 2),
        (10, [10, 71, 84, 33, 6, 47, 23, 25, 52, 64], 36),
        (7, [1, 2, 3, 1000000000, 4, 5, 6], 999999994),
    ]

    for N, A, ans in NA_ans:
        assert TLE(N, A) == ans
        assert f(N, A) == ans


def f(N, A):
    ans = float("inf")
    S = A[::]
    for i in range(1, N):
        S[i] += S[i-1]

    for mid in range(2, N-1):
        # 均等
        x = S[mid-1] / 2
        left = bisect_right(S, x)
        if abs(S[left-1] - x) < abs(S[left] - x):
            left -= 1

        y = (S[-1] + S[mid-1]) / 2
        right = bisect_right(S, y)
        if abs(S[right-1] - y) < abs(S[right] - y):
            right -= 1

        p = S[left]
        q = S[mid-1] - S[left]
        r = S[right] - S[mid-1]
        s = S[-1] - S[right]
        sums = (p, q, r, s)
        ans = min(ans, max(sums) - min(sums))

    return ans


def TLE(N, A):
    ans = float("inf")
    for b in range(1, N-2):
        for c in range(b+1, N-1):
            for d in range(c+1, N):
                B = A[:b]
                C = A[b:c]
                D = A[c:d]
                E = A[d:]
                print(B, C, D, E)

                *sums, = map(sum, [B, C, D, E])
                x = abs(max(sums) - min(sums))
                ans = min(ans, x)

    return ans


if __name__ == '__main__':
    main()
