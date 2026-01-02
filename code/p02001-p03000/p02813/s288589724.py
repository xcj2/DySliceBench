#!/usr/bin/env python3
import sys
import itertools

def solve(N: int, P: "List[int]", Q: "List[int]"):
    if P == Q:
        print(0)
        return 
    all = list(itertools.permutations(list(range(1,N+1)))) 
    a = None
    b = None
    P = tuple(P)
    Q = tuple(Q)
    for i in range(len(all)):
        if all[i] == P:
            a = i
        elif all[i] == Q:
            b = i
    
    print(abs(a-b))

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    Q = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, P, Q)

if __name__ == '__main__':
    main()
