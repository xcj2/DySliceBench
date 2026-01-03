#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(S: str):
    def count(s):
        tmp = s[0]
        cnt = 0
        for c in s:
            if c != tmp:
                cnt += 1
                tmp = c
        return cnt
    #ret = min(count(S), count(str(reversed(list(S)))))
    ret = count(S)
    print(ret)
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
