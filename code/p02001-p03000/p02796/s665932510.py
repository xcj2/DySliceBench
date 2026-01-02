#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, X: "List[int]", L: "List[int]"):

    # 区間に変換する
    segs = [(x-l, x+l) for x, l in zip(X, L)]
    segs.sort(key=lambda x: x[1])  # 尻でソート

    # DP i個目の区間まで考えた時の残せる数
    DP = [0]*N
    DP[0] = 1
    for i in range(1, N):
        # 重なっていなければ
        if segs[i-1][1] <= segs[i][0]:
            DP[i] = DP[i-1]+1
        else:
            # 加えないか
            DP[i] = DP[i-1]
            # 重なるものを抜いた場合の個数+1
            left = -1
            right = i-1
            while right-left > 1:
                mid = (right+left)//2
                if segs[mid][1] <= segs[i][0]:
                    left = mid
                else:
                    right = mid
            # すべて重なるケースは区別
            if left == -1:
                buf = 1
            else:
                buf = DP[left]+1
            DP[i] = max(buf, DP[i-1])
    print(DP[-1])

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    L = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        L[i] = int(next(tokens))
    solve(N, X, L)


if __name__ == '__main__':
    main()
