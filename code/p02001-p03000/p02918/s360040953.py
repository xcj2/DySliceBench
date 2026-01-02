#!/usr/bin/env python3
import sys
from itertools import groupby
## 幸福数はN-group数
def solve(N: int, K: int, S: str):
    groups = groupby(S)
    compress = []
    for key,group in groups:
        compress.append(key)

    print(min(N-1,N-(len(compress)-2*K)))

    
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, K, S)

if __name__ == '__main__':
    main()
