#!/usr/bin/env python3
import sys
from bisect import bisect_left
from collections import Counter
INF = float("inf")


def yes():
    print("Yes")  # type: str


def no():
    print("No")  # type: str


def solve(N: int, a: "List[int]"):
    cnt = Counter(a)
    v = list(cnt.values())
    b = list(cnt.keys())
    if len(cnt) == 3:
        if all([x == v[0] for x in v]):
            if b[0] ^ b[1] == b[2] or b[0] ^ b[2] == b[1]:
                yes()
                return
    elif len(cnt) == 2:
        if b[0] != 0:
            b[1], b[0] = b[0], b[1]
        if b[0] == 0 and cnt[b[1]] == cnt[b[0]]*2:
            yes()
            return

    elif len(cnt) == 1:
        if b[0] == 0:
            yes()
            return

    no()
    return

    # print(*keta, sep="\n")
    # def solve(N: int, a: "List[int]"):
    #     a.sort()
    #     used = Counter(a)
    #     used_orig = used.copy()
    #     x = [a[0]]
    #     used[0] -= 1

    #     # print("first, ", a[0])
    #     # 2番目の帽子を全探索
    #     for i in range(1, N):
    #         # print("2nd, ", a[i])
    #         x.append(a[i])
    #         used[i] -= 1
    #         for j in range(2, N):
    #             cand = x[-1] ^ x[-2]
    #             # print("cand, ", cand)
    #             pl = bisect_left(a, cand)
    #             if pl >= len(a):
    #                 break
    #             if cand == a[pl] and used[cand] > 0:
    #                 x.append(cand)
    #                 used[pl] -= 1
    #             else:
    #                 break
    #         else:
    #             yes()
    #             print(x)
    #             print(used)
    #             return
    #         x = [a[0]]
    #         used = used_orig.copy()
    #     no()
    #     return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)


if __name__ == '__main__':
    main()
