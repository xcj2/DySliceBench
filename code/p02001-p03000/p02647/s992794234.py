#create date: 2020-06-14 10:29

import sys
stdin = sys.stdin
from itertools import accumulate

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    n, k = na()
    a = na()
    def step():
        b = [0] * n
        for i, ai in enumerate(a):
            start, stop = i - ai, i + ai + 1
            if start > 0:
                b[start] += 1
            else:
                b[0] += 1
            if stop < n:
                b[stop] -= 1
        return list(accumulate(b))

    for i in range(k):
        anext = step()
        if sum(a) == sum(anext):
            print(*a)
            quit()
        a = anext
    print(*a)


if __name__ == "__main__":
    main()