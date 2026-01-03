#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, K: int, D: "List[int]"):
    tmp = N
    while True:
        i = tmp
        ng = False
        while i > 0:
            if (i % 10) in D:
                ng = True
                break
            i //= 10
        if not ng:
            print(tmp)
            return
        tmp += 1
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    D = [ int(next(tokens)) for _ in range(K) ]  # type: "List[int]"
    solve(N, K, D)

if __name__ == '__main__':
    main()
