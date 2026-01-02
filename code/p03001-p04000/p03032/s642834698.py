#!/usr/bin/env python3
import sys
from heapq import heapify, heappop

def solve(N: int, K: int, V: "List[int]"):
    ans = 0
    for n_all in range(min(N, K)+1):
        for n_l in range(n_all+1):
            n_r = n_all - n_l
            tmp_v = V[:n_l] + V[N-n_r:]
            heapify(tmp_v)
            i = 0
            while len(tmp_v) > 0 and tmp_v[0] < 0 and i < K-n_all:
                _ = heappop(tmp_v)
                i += 1
            ans = max(ans, sum(tmp_v))
    print(ans)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    V = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, K, V)

if __name__ == '__main__':
    main()
