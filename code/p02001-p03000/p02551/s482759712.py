import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
MOD = 1000000007


def main():
    N, Q, *queries = map(int, read().split())
    queries = [(q, x) for q, x in zip(*[iter(queries)] * 2)]

    N -= 2

    # N: 処理する区間の長さ

    N0 = 2 ** (N - 1).bit_length()
    data1 = [None] * (2 * N0)
    data2 = [None] * (2 * N0)
    INF = (-1, 2 ** 31 - 1)
    # 区間[l, r+1)の値をvに書き換える
    # vは(t, value)という値にする (新しい値ほどtは大きくなる)
    def update(l, r, v, data):
        L = l + N0
        R = r + N0
        while L < R:
            if R & 1:
                R -= 1
                data[R - 1] = v

            if L & 1:
                data[L - 1] = v
                L += 1
            L >>= 1
            R >>= 1

    # a_iの現在の値を取得
    def _query(k, data):
        k += N0 - 1
        s = INF
        while k >= 0:
            if data[k]:
                s = max(s, data[k])
            k = (k - 1) // 2
        return s

    # これを呼び出す
    def query(k, data):
        return _query(k, data)[1]

    update(0, N, (0, N), data1)
    update(0, N, (0, N), data2)

    min1 = min2 = N + 10
    ans = N * N

    for i, (q, x) in enumerate(queries, 1):
        x -= 2
        if q == 1:
            data = data1
            this_min = min1
        else:
            data = data2
            this_min = min2

        n = query(x, data)
        ans -= n

        if x > this_min:
            continue

        if q == 1:
            min1 = x
            update(0, n, (i, x), data2)
        else:
            min2 = x
            update(0, n, (i, x), data1)

    print(ans)
    return


if __name__ == '__main__':
    main()
