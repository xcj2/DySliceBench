#!/usr/bin/env python3
import sys

YES = "POSSIBLE"  # type: str
NO = "IMPOSSIBLE"  # type: str
import bisect

def solve(N: int, M: int, a: "List[int]", b: "List[int]"):
    ab = list(zip(a,b))
    ab.sort(key=lambda x: x[0])
    a.sort()

    for aabb in ab:
        if aabb[0] != 1:
            break 

        next_index = bisect.bisect_left(a,aabb[1])
        next_index2 = bisect.bisect_left(a,aabb[1]+1)

        for i in range(next_index,next_index2):
            if ab[i][1] == N:
                print(YES)
                return

    print(NO)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int()] * (M)  # type: "List[int]"
    b = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, M, a, b)

if __name__ == '__main__':
    main()
