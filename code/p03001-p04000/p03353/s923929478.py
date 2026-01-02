#!/usr/bin/env python3
import sys


def solve_(S: str, K: int, used):
    #print(S, K, used)
    mn = 'z'
    tmp = set()
    for i, c in enumerate(S):
        if c < mn and not c in used:
            tmp = set()
            for j in range(5):
                tmp.add(S[i:i + j + 1])
            mn = c
        elif c == mn:
            for j in range(5):
                tmp.add(S[i:i + j + 1])
    if len(tmp) < K:
        used.append(mn)
        return solve_(S, K - len(tmp), used)
    else:
        tmp = list(tmp)
        tmp.sort()
        return tmp[K - 1]

def solve(S, K):
    ret = solve_(S, K, [])
    print(ret)
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
