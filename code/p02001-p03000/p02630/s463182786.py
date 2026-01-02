#create date: 2020-06-29 09:42

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    n = ni()
    a = na()
    alist = [0] * (10**5 + 1)
    for ai in a:
        alist[ai] += 1
    asum = 0
    for i, num in enumerate(alist):
            asum += i*num

    q = ni()
    for i in range(q):
        b, c = na()
        asum += alist[b] * (c-b)
        alist[c] += alist[b]
        alist[b] = 0
        print(asum)

if __name__ == "__main__":
    main()