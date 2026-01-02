#!/usr/bin/env python3
import sys
import bisect

def solve(N: int, L: "List[int]"):
    L.sort()
    answer = 0
    for i in range(N):
        for j in range(i+1,N):
            max_k = bisect.bisect_left(L,L[i]+L[j])
            answer += max_k-(j+1)
    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    L = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, L)

if __name__ == '__main__':
    main()
