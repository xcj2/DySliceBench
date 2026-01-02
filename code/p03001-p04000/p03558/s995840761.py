from collections import deque


def main():
    """K の正の倍数の 10 進法での各桁の和としてありうる最小の値を求めてください。

    2 ≤ K ≤ 10^5

    min: 1が1つと他が0 -> 10^n, e.g.: 5*2, 25*4
    10倍しても元のKと和は変わらない
    1-9倍とは限らない?: 入力例 2　11111=41×271, 4+1=5では？
    """
    K = int(input())

    ans = sum_digits(K)
    for i in range(2, 10):
        ans = min(ans, sum_digits(K * i))

    print(ans)


def sum_digits(n):
    return sum(map(int, list(str(n))))


def main2():
    import sys

    debug = sys.argv[-1] == "debug"
    K = int(input())

    q = deque([1])
    inf = float("inf")
    dp = [inf for _ in range(K)]
    dp[1] = 0

    # 01BFS
    # cost 0 の辺の遷移は deque の先頭に要素を追加
    # cost 1 の辺の遷移は deque の末尾に要素を追加
    while q:
        idx = q.popleft()
        x = dp[idx]
        m1 = (idx * 10) % K
        m2 = (idx + 1) % K
        if dp[m1] > x:
            dp[m1] = x
            q.appendleft(m1)
        if dp[m2] > x + 1:
            dp[m2] = x + 1
            q.append(m2)

        if debug:
            print((m1, m2), dp, q, file=sys.stderr)
            print("-" * 10, file=sys.stderr)

    print(dp[0] + 1)


if __name__ == '__main__':
    main2()
