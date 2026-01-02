# この提出を含めて
# この時間までに提出している私のすべてのBの提出は嘘解法でした

# ランダムに作成した下記のテストケースで解答が不一致でした

# 6 2 5 3
# 6 4 3 2 1 1

# https://atcoder.jp/contests/agc041/submissions/9179921
# 4

# 自分
# 6

def main():
    from bisect import bisect_left, bisect_right
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    N, M, V, P = map(int, input().split())
    *A, = sorted(map(int, input().split()))
    acc = (0,) + tuple(accumulate(A))

    def is_ok(mid):
        x = A[mid]
        ika = bisect_right(A, x)
        rest = max(0, V - ika)
        if rest >= P:
            # 上位P-1に毎回加算して、
            # rest-(P-1)人に対し、最大値を上げないようにして、均等に割り振る
            rng = N - ika - (P - 1)  # 加算先候補数
            times = V - (P - 1) - ika  # M人のjudgeがtimes回加算する

            range_sum = acc[mid + 1 + rng] - acc[mid + 1]
            to_sub = A[mid + rng] * rng - range_sum
            to_dist = M * times - to_sub

            if to_dist <= 0:
                return A[N - P] <= x + M
            else:
                to_add = (to_dist + rng - 1) // rng
                return max(A[N - P], A[mid + rng] + to_add) <= x + M

        else:
            return A[N - P] <= x + M

    def binary_search():
        ok = N - 1
        ng = -1
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    idx = binary_search()
    print(N - bisect_left(A, A[idx]))


if __name__ == '__main__':
    main()
