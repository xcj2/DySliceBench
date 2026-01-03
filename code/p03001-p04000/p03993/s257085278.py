#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32
from bisect import bisect_left, bisect_right

def solve(N: int, a: "List[int]"):
    # x = [[i+1, a[i]] for i in range(N)]

    # x = sorted(x, key=lambda x:x[1])
    # x1 = [i for i,j in x]
    # x2 = [j for i,j in x]

    # ans = 0
    # for i in range(N):
    #     p = bisect_left(x2, x1[i])
    #     if not (0 <= p < N):
    #         continue
    #     if x1[i] == x2[p] and x2[i] == x1[p]:
    #         ans += 1

    # print(ans//2)

    ans = 0
    for i in range(N):
        if a[a[i]-1] == i+1:
            ans += 1

    print(ans//2)


    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
