#!/usr/bin/env python3
import sys
import math
import bisect

def solve(n: int, a: "List[int]"):
    if n == 2:
        print(*sorted(a,reverse=True))
        return 

    a.sort()
    max_a = a[-1]


    if max_a%2 ==1:
        searchValue = max_a//2+1
    else:
        searchValue = max_a//2

    index = bisect.bisect_left(a,searchValue)
    if abs(max_a/2-a[index]) > abs(max_a/2-a[index-1]):
        print(max_a,a[index-1])
    else:
        print(max_a,a[index])

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(n)]  # type: "List[int]"
    solve(n, a)

if __name__ == '__main__':
    main()
