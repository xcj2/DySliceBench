#!/usr/bin/env python3
import sys
from bisect import bisect_left

def solve(N: int, Q: int, S: str, l: "List[int]", r: "List[int]"):
    A_index = []
    ## ACの場所を全部記録しときたい→Aの場所を全部記録
    for i in range(N-1):
        if S[i] == 'A' and S[i+1] == 'C':
            A_index.append(i)
    
    for j in range(Q):
        if r[j] <= 1:
            print(0)
            continue

        left_index = bisect_left(A_index,l[j]-1)
        right_index = bisect_left(A_index,r[j]-1)
        print(right_index-left_index)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    l = [int()] * (Q)  # type: "List[int]"
    r = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        l[i] = int(next(tokens))
        r[i] = int(next(tokens))
    solve(N, Q, S, l, r)

if __name__ == '__main__':
    main()
