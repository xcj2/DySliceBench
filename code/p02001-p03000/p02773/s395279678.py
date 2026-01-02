#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, S: "List[str]"):
    c = {}
    for s in S:
        if not s in c:
            c[s] = 0
        c[s] += 1
    tmp =list( c.items())
    tmp.sort(key = lambda x: (-x[1], x[0]))
    ret = [tmp[0][0]]
    for i in range(1, len(tmp)):
        if tmp[i][1] == tmp[0][1]:
            ret.append(tmp[i][0])
        else:
            break
    for r in ret:
        print(r)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, S)

if __name__ == '__main__':
    main()
