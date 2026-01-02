#!/usr/bin/env python3
import sys
from bisect import bisect_left
from itertools import accumulate

INF = float("inf")


def solve(N: int, M: int, A: "List[int]"):
    A.sort()

    # 幸福度X以上を得られる握手をカウントし、M以上となる境界を探す
    # Xが小さい方が握手の個数は多く、Xが大きい方が握手の個数は少ない
    left = 0
    right = 3*(10**5)
    while right - left > 1:
        X = (right + left)//2

        # 握手の個数は、左手を固定した上で、右手をにぶたんする。
        tot = 0
        for left_hand in A:
            tot += N-bisect_left(A, X-left_hand)

        if tot < M:
            right = X
        else:
            left = X

    # print(left, right)
    # 幸福度rightを得られる握手はM個未満
    # 幸福度leftを得られる握手はM個以上

    # 幸福度rightを得られる握手をすべてカウントした上で、
    # 不足する個数だけ、幸福度leftを加える
    happy = 0

    acc = [0]+list(accumulate(A))
    tot = 0
    for left_hand in A:
        i = bisect_left(A, right-left_hand)
        tot += N-i
        happy += (acc[N]-acc[i]) + left_hand*(N-i)

    happy += (M-tot)*left
    print(happy)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, A)


if __name__ == '__main__':
    main()
