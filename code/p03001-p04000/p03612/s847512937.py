#!/usr/bin/env python3
import sys
from math import ceil

def solve(N: int, p: "List[int]"):
    ng_check = [0]*N

    for i in range(N):
        if i+1 == p[i]:
            ng_check[i] = 1
    
    answer = 0
    from itertools import groupby
    group = groupby(ng_check)
    for key,gr in group:
        if key == 0:
            continue

        answer += ceil(len(list(gr))/2)
    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    p = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, p)

if __name__ == '__main__':
    main()
