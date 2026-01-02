#!/usr/bin/env python3
import sys


def solve(N: int, M: int, A: "List[int]"):
    cur = 0
    counts = {0 : 1}
    for a in A:
        cur = (cur + a) % M
        if cur in counts:
            counts[cur] += 1
        else:
            counts[cur] = 1
    ret = 0
    #print(counts)
    for val in counts.values():
        #print(val)
        ret += val * (val - 1) // 2
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, M, A)

if __name__ == '__main__':
    main()
