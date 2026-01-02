#!/usr/bin/env python3
import sys


def solve(X: int, Y: int, A: int, B: int, C: int, p: "List[int]", q: "List[int]", r: "List[int]"):
    pqr = [(0,p[i]) for i in range(A)] + [(1,q[i]) for i in range(B)] + [(2,r[i]) for i in range(C)]
    pqr.sort(key= lambda x: -x[1])

    answer = 0
    count = [0,0,0]
    for i in range(len(pqr)):
        if sum(count) == X+Y:
            break
        key,value = pqr[i]
        if key == 0:
            if count[key] >= X:
                continue
            count[key] += 1
        elif key == 1:
            if count[key] >= Y:
                continue
            count[key] += 1
        else:
            count[key] += 1
        answer += value
    
    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    p = [int(next(tokens)) for _ in range(A)]  # type: "List[int]"
    q = [int(next(tokens)) for _ in range(B)]  # type: "List[int]"
    r = [int(next(tokens)) for _ in range(C)]  # type: "List[int]"
    solve(X, Y, A, B, C, p, q, r)

if __name__ == '__main__':
    main()
