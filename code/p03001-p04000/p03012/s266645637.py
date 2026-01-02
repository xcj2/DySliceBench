#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)
INF = 1<<32


def solve(N: int, W: "List[int]"):
    ans = INF
    for i in range(N):
        # s1 = [W[j] for j in range(N) if W[j] <= W[i]]
        # s2 = [W[j] for j in range(N) if W[j] > W[i]]
        s1 = W[:i]
        s2 = W[i:]
        # print(W[i], s1, s2, sum(s1), sum(s2), abs(sum(s1)-sum(s2)))
        ans = min(ans, abs(sum(s2)-sum(s1)))

    print(ans)
    return  



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    W = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, W)

if __name__ == '__main__':
    main()
