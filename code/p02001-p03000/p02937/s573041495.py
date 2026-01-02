#!/usr/bin/env python3
import sys
from bisect import bisect_left
from collections import defaultdict
INF = float("inf")


def solve(s: str, t: str):

    S = len(s)
    T = len(t)
    ABC = defaultdict(list)
    for i, c in enumerate(s):
        ABC[c].append(i)

    counter = 0
    head = 0
    # print(ABC)
    for tt in t:
        if len(ABC[tt]) == 0:
            print(-1)
            return
        j = bisect_left(ABC[tt], head) % len(ABC[tt])
        counter += (ABC[tt][j]-head) % S + 1
        # print(tt, ABC[tt], j, ABC[tt][j], "head:",
        # head, ",counter:", counter, S)
        head = (ABC[tt][j]+1) % S
    print(counter)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    t = next(tokens)  # type: str
    solve(s, t)


if __name__ == '__main__':
    main()
