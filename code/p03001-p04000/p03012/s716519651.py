#!/usr/bin/env python3
import sys
from itertools import accumulate

def solve(N: int, W: "List[int]"):
    #print(W)
    sumL = sum(W)
    sumR = 0
    ans = abs(sumL-sumR)
    for i in range(N):
        sumL -= W[i]
        sumR += W[i]
        ans = min(ans, abs(sumL-sumR))
    print(ans)

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    W = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, W)

if __name__ == '__main__':
    main()
