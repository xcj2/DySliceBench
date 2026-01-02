#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, H: "List[int]"):
    ## 右側に2以上低いものがあったら不可能

    cur_max = 0
    for i in range(N):
        if cur_max - H[i] >= 2:
            print(NO)
            return 
        cur_max = max(cur_max,H[i])
    print(YES)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    H = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, H)

if __name__ == '__main__':
    main()
