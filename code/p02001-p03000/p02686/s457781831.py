#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
INF = float("inf")


def yes():
    print("Yes")  # type: str


def no():
    print("No")  # type: str


def solve(N: int, S: "List[str]"):

    def seq_positive(ls):
        state = 0
        for l, st in ls:
            if state+l < 0:
                return False
            state += st
        return True

    # 部分括弧列の特徴量を計算する。
    # 経過中の最小値と、最終到達値
    left_seq = []
    right_seq = []
    total = 0
    for s in S:
        state = 0
        lower = 0
        for c in s:
            if c == "(":
                state += 1
            else:
                state -= 1
            lower = min(lower, state)
        if state > 0:
            left_seq.append((lower, state))
        else:
            right_seq.append((lower-state, -state))
        total += state

    left_seq.sort(reverse=True)
    right_seq.sort(reverse=True)
    # print(left_seq)
    # print(right_seq)

    if seq_positive(left_seq) and seq_positive(right_seq) and total == 0:
        yes()
    else:
        no()

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, S)


if __name__ == '__main__':
    main()
