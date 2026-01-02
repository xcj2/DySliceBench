#!/usr/bin/env python3.4

# abc128_d

import collections
import itertools

def find_index(iterable, func):
    i = 0
    for it in iterable:
        if func(it):
            break
        i += 1
    return i

def slice_deq(deq, n):
    return itertools.islice(deq, 0, n)

def main():
    # Input
    n, k = [int(s) for s in input().split()]
    vs = (int(s) for s in input().split())
    # Get ans
    vs = collections.deque(vs)
    R = min(n, k)
    def gene_tv():
        for i in range(1, R+1):
            vs.rotate(-1)
            vs.reverse()
            for _ in range(i+1):
                temp = list(slice_deq(vs, i))
                temp.sort()
                l = find_index(temp, lambda x: x>0)
                l = min(l, k-i)
                yield sum(temp[l:])
                vs.rotate(-1)
            vs.rotate(-(i-1))
    ans = max(gene_tv())
    ans = max(ans, 0)
    # Output
    print(ans)

if __name__ == '__main__':
    main()

