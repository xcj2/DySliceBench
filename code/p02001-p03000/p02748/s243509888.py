#!/usr/bin/env python3
import sys


def solve(A: int, B: int, M: int, a: "List[int]", b: "List[int]", x: "List[int]", y: "List[int]", c: "List[int]"):
    # sort_a = sorted(enumerate(a),key=lambda x: x[1])
    MINB = min(b)
    # print(sort_a)
    waribiki = [[] for _ in range(A)]
    for i in range(M):
        waribiki[x[i]-1].append((y[i]-1,c[i]))
    
    answer = 10**18

    for i in range(A):
        aa = a[i]
        for b_idx,cc in waribiki[i]:
            answer = min(aa+b[b_idx]-cc,answer)
        
        answer = min(aa+MINB,answer)
    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(A)]  # type: "List[int]"
    b = [int(next(tokens)) for _ in range(B)]  # type: "List[int]"
    x = [int()] * (M)  # type: "List[int]"
    y = [int()] * (M)  # type: "List[int]"
    c = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(A, B, M, a, b, x, y, c)

if __name__ == '__main__':
    main()
