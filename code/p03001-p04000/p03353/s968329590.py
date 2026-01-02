#!/usr/bin/env python3
import sys


def solve(s: str, K: int):

    candidate = set()
    N = len(s)
    for length in range(1,K+1):
        for i in range(N):
            if i+length>N:
                break
            candidate.add(s[i:i+length])
    
    candidate = sorted(list(candidate))
    print(candidate[K-1])
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    K = int(next(tokens))  # type: int
    solve(s, K)

if __name__ == '__main__':
    main()
