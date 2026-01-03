#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)

MOD = 1000000007  # type: int

def solve(N: int, A: "List[int]"):
    count = [0] * N
    for a in A:
        if a % 2 == N % 2:
            print(0)
            return
        count[a] += 1
    if N % 2 == 1 and count[0] == 1:
        count = count[1:]
    for cnt in count:
        if cnt != 0 and cnt != 2:
            print(0)
            return
    ret = (2 ** (N // 2)) % MOD
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
