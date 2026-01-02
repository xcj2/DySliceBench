#!/usr/bin/env python3.4

# abc128_d

import collections
import itertools

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
                tv = 0
                pps = []
                for v in slice_deq(vs, i):
                    tv += v
                    if v<0:
                        pps.append(v)
                #print(i, vs, tv, pps)
                vs.rotate(-1)
                pps.sort()
                pp = sum(pps[:k-i])
                yield tv-pp
            vs.rotate(-(i-1))
    ans = max(gene_tv())
    ans = max(ans, 0)
    # Output
    print(ans)

if __name__ == '__main__':
    main()

