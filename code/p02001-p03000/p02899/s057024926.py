#!/usr/bin/env python3
import sys
import numpy as np


def solve(N: int, A: "List[int]"):
    npA = np.array(A)
    std = np.argsort(npA)+1
    std = std.tolist()
    n = [str(n) for n in std]
    print(' '.join(n))




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
