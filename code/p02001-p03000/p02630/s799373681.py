#create date: 2020-06-29 09:42

import sys
stdin = sys.stdin
from collections import defaultdict

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    n = ni()
    a = na()
    counter = defaultdict(int)
    for ai in a:
        counter[ai] += 1
    asum = sum(a)

    q = ni()
    for i in range(q):
        b, c = na()
        asum += counter[b] * (c-b)
        counter[c] += counter[b]
        counter[b] = 0
        print(asum)

if __name__ == "__main__":
    main()