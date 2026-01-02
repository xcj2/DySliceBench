#!/usr/bin/env python3
import sys
from collections import Counter
INF = float("inf")


def solve(N: int, A: "List[int]"):
    counter = Counter(A)
    # 作れるか
    count = 0
    cand = []
    for k in counter:
        if counter[k] >= 4:
            cand.append(k)
            cand.append(k)
        elif counter[k] >= 2:
            cand.append(k)
    if len(cand) < 2:
        print(0)
        return
    else:
        cand.sort(reverse=True)
        area = cand[0]*cand[1]
        print(area)
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
