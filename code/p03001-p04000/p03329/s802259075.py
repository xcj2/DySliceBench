def main():
    """
    1 <= N <= 10^5
    """
    N = int(input())

    ans = rec(N)
    print(ans)


def test_ans():
    N_ans = [
        (127, 4),
        (3, 3),
        (44852, 16),
    ]
    for N, ans in N_ans:
        assert rec(N) == ans


def rec(N):
    import sys
    sys.setrecursionlimit(10 ** 7)
    memo = [-1] * (N+1)

    def _rec(i):
        if i == 0:
            return 0
        if memo[i] != -1:
            return memo[i]

        ans = N
        p = 1
        while p <= i:
            #print(6, i, i-p)
            ans = min(ans, _rec(i-p) + 1)
            p *= 6
        p = 1
        while p <= i:
            #print(9, i, i-p)
            ans = min(ans, _rec(i-p) + 1)
            p *= 9

        memo[i] = ans

        return ans

    ans = _rec(N)
    return ans


if __name__ == '__main__':
    main()
