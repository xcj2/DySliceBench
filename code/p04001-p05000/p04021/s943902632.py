#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, A: "List[int]"):

    # Aを0~N-1に付け直す
    dic = {}
    for i, a in enumerate(sorted(A)):
        dic[a] = i
    B = [dic[a] for a in A]

    # Bの内、偶数番目にある奇数の数だけ操作1が必要
    count = 0
    for i in range(0, N, 2):
        if B[i] % 2 == 1:
            count += 1
    print(count)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)


if __name__ == '__main__':
    main()
