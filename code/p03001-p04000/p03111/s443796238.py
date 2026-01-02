#!/usr/bin/env python3
import sys
INF = float('inf')

def solve(N: int, A: int, B: int, C: int, l: "List[int]"):
    target = [A, B, C]
    def calc(group):
        ret = 0
        for i in range(3):
            elms = group[i]
            if len(elms) < 1:
                return INF
            ret += (len(elms) - 1) * 10
            total = 0
            for e in elms:
                total += l[e]
            ret += abs(total - target[i])
        return ret

    def rec(idx, group):
        if idx >= N:
            return calc(group)
        ret = INF
        for i in range(4):
            group[i].append(idx)
            ret = min(ret, rec(idx + 1, group))
            group[i].remove(idx)
        return ret

    ret = rec(0, [[] for i in range(4)])
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    l = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, A, B, C, l)

if __name__ == '__main__':
    main()
