#!/usr/bin/env python3
import sys
import math

def solve(N: int, H: int, a: "List[int]", b: "List[int]"):
    ab = list(zip(a,b))

    max_a = 0
    for i in range(N):
        if max_a < a[i]:
            max_a = a[i]

    b_sort = sorted(ab,key=lambda x: -x[1])
    answer = 0
    Hitpoint = H

    for _,bb in b_sort:
        ## 最初高いものから刀を投げつけて、最後に切る
        if bb <= max_a:
            break

        Hitpoint -= bb
        answer += 1

        if Hitpoint <= 0:
            print(answer)
            return
    answer += math.ceil(Hitpoint/max_a)
    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    H = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    b = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, H, a, b)

if __name__ == '__main__':
    main()
