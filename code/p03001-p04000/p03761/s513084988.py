#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(n: int, S: "List[str]"):
    ret = ''
    counts = [[0] * n for _ in range(26)]
    for i, s in enumerate(S):
        for c in s:
            counts[ord(c) - ord('a')][i] += 1
    #print(counts)
    for i, cnt in enumerate(counts):
        ret += ''.join([chr(ord('a') + i) for _ in range(min(cnt))])
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    S = [ next(tokens) for _ in range(n) ]  # type: "List[str]"
    solve(n, S)

if __name__ == '__main__':
    main()
