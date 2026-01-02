from itertools import product
from bisect import bisect_left, bisect_right


def main():
    A, B, Q = map(int, input().split())
    ss = [int(input()) for _ in range(A)]
    ts = [int(input()) for _ in range(B)]
    xs = [int(input()) for _ in range(Q)]

    # gen = TLE(A, B, Q, ss, ts, xs)
    # gen = f(A, B, Q, ss, ts, xs)
    gen = editorial(A, B, Q, ss, ts, xs)
    print(*gen, sep="\n")


def TLE(A, B, Q, ss, ts, xs):
    for x in xs:
        ans = float("inf")
        for s in ss:
            for t in ts:
                if s <= x <= t or t <= x <= s:
                    ds, dt = abs(x-s), abs(x-t)
                    tmp = min(ds, dt) + abs(s-t)
                elif x <= s <= t or x <= t <= s:
                    tmp = max(s, t)-x
                elif x >= s >= t or x >= t >= s:
                    tmp = x-min(s, t)
                ans = min(ans, tmp)

        yield ans


def f_ans(s, t, x):
    if s <= x <= t or t <= x <= s:
        ds, dt = abs(x-s), abs(x-t)
        tmp = min(ds, dt) + abs(s-t)
    elif x <= s <= t or x <= t <= s:
        tmp = max(s, t)-x
    elif x >= s >= t or x >= t >= s:
        tmp = x-min(s, t)
    return tmp


def f(A, B, Q, ss, ts, xs):
    for x in xs:
        t_left = bisect_left(ts, x)
        t_right = bisect_right(ts, x)
        s_left = bisect_left(ss, x)
        s_right = bisect_right(ss, x)

        t_idx = [t_right + a for a in [-1, 0, 1]]
        t_idx += [t_left + a for a in [-1, 0, 1]]
        s_idx = [s_right + a for a in [-1, 0, 1]]
        s_idx += [s_left + a for a in [-1, 0, 1]]

        ans = float("inf")
        for si, ti in product(set(s_idx), set(t_idx)):
            if 0 <= si < A and 0 <= ti < B:
                tmp = f_ans(ss[si], ts[ti], x)
                ans = min(ans, tmp)
        yield ans


def editorial(A, B, Q, ss, ts, xs):
    INF = float("inf")
    # 番兵
    ss = [-INF] + ss + [INF]
    ts = [-INF] + ts + [INF]
    for x in xs:
        # -inf の右 [1]
        # +inf の左 [-1]
        b, d = bisect_right(ss, x), bisect_right(ts, x)
        ans = INF
        # 番兵のおかげでindex を気にしなくて良い
        for s in [ss[b - 1], ss[b]]:
            for t in [ts[d - 1], ts[d]]:
                # s--t--x, t--s--x
                # s--x--t, t--x--s
                # x--t--s, x--s--t
                d1 = abs(s - x) + abs(t - s)
                d2 = abs(t - x) + abs(s - t)
                ans = min(ans, d1, d2)

        yield ans


if __name__ == "__main__":
    main()
