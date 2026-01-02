#!/usr/bin/env python3
import sys
from itertools import accumulate
INF = float("inf")


def solve(N: int, C: int, s: "List[int]", t: "List[int]", c: "List[int]"):
    seq = [0]*(3*10**5)
    # チャンネルを切り替えない場合、0.5秒のラグが発生しない。
    # 同じチャンネルでしりとあたまがいっしょなら、ひとつの番組にしておく
    c, s, t = zip(*sorted(sorted(zip(c, s, t), key=lambda x: x[1])))
    # いもす法
    # seq = [0]*(40)
    pre_s, pre_t, pre_c = -1, -1, -1
    for sv, tv, cv in zip(s, t, c):
        if pre_c == cv and pre_t == sv:
            seq[2*pre_t] += 1
            seq[2*tv] -= 1
        else:
            seq[2*sv-1] += 1
            seq[2*tv] -= 1
        pre_s, pre_t, pre_c = sv, tv, cv
    acc = list(accumulate(seq))
    # print(seq)
    # print(acc)
    print(max(acc))
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    s = [int()] * (N)  # type: "List[int]"
    t = [int()] * (N)  # type: "List[int]"
    c = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        s[i] = int(next(tokens))
        t[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(N, C, s, t, c)


if __name__ == '__main__':
    main()
