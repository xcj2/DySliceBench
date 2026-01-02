#!/usr/bin/env python3
import sys


def solve(N: int, s: "List[str]", M: int, t: "List[str]"):
    dic = {}
    for a in s:
        if a in dic:
            dic[a] += 1
        else:
            dic[a] = 1
    for a in t:
        if a in dic:
            dic[a] -= 1
        else:
            dic[a] = -1
    ret = 0
    for val in dic.values():
        ret = max(ret, val)
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    s = [ next(tokens) for _ in range(N) ]  # type: "List[str]"
    M = int(next(tokens))  # type: int
    t = [ next(tokens) for _ in range(M) ]  # type: "List[str]"
    solve(N, s, M, t)

if __name__ == '__main__':
    main()
