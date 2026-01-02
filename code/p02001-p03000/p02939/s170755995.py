#!/usr/bin/env python3
import sys


def solve(S: str):
    start = 0
    answer = 0
    s = ""
    prev = ""
    while start < len(S):
        s += S[start]
        if prev == s:
            start +=1
            continue
        else:
            prev = s
            s = ""
            start +=1
            answer +=1
    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)

if __name__ == '__main__':
    main()
