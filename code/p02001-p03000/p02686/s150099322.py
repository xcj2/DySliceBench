#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
INF = float("inf")


def yes():
    print("Yes")  # type: str


def no():
    print("No")  # type: str


def solve(N: int, S: "List[str]"):

    def f(s):
        ans = [0]*(len(s)+1)
        m = 0
        for i, c in enumerate(s):
            if c == "(":
                m += 1
            else:
                m -= 1
            ans[i] = m
        return min(*ans), m, s

    # 数値化(最小値, 到達値)
    T = [f(s) for s in S]

    front = []
    back = []
    for a, b, s in T:
        if b >= 0:
            front.append((a, b, s))
        else:
            back.append((a, b, s))

    front.sort(key=lambda x: x[0], reverse=True)
    back.sort(key=lambda x: min(0, x[0]-x[1]), reverse=True)
    # print(front)
    # print(back)

    m = 0
    for ma, mb, s in front+back[::-1]:
        if m + ma < 0:
            no()
            # print("負", s)
            return
        m += mb

    if m == 0:
        yes()
    else:
        # print("非零到達")
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
