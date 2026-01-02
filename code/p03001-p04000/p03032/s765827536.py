#!/usr/bin/env python3.4

# abc128_d

import collections

def find_index(iterable, func):
    i = 0
    for it in iterable:
        if func(it):
            break
        i += 1
    return i

def main():
    # Input
    n, k = [int(s) for s in input().split()]
    vs = [int(s) for s in input().split()]
    # Get ans
    R = min(n, k)
    def gene_lr():
        for i in range(1, R+1):
            for j in range(i+1):
                yield(i-j, j)
    def gene_tv():
        for l, r in gene_lr():
            tv = 0
            temp = vs[:l] + vs[n-r:]
            temp.sort()
            i = find_index(temp, lambda x: x>0)
            s = k-(l+r)
            s = min(i, s)
            yield sum(temp[s:])
    ans = max(gene_tv())
    ans = max(ans, 0)
    # Output
    print(ans)

if __name__ == '__main__':
    main()

