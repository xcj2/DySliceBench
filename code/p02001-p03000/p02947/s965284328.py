#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, S: "List[str]"):
    p = []
    count = {}
    for i, s in enumerate(S):
        s = list(s)
        s.sort()
        s = ''.join(s)
        if s in count:
            count[s] += 1
        else:
            count[s] = 1
        p.append(s)
    ret = 0
    #for v in p:
    #    print(count[s])
    #    ret += len(count[s])
    for c in count.values():
        ret += c * (c - 1) // 2
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
    solve(N, s)

if __name__ == '__main__':
    main()
