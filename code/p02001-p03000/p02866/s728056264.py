#!/usr/bin/env python
# coding: utf-8

from collections import Counter
def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

def main():
    n = ri()
    ld = rli()
    if ld[0] != 0:
        print(0)
        return
    counter = Counter()
    for d in ld:
        counter[d] += 1
    cnt = 0
    ans = 1
    bef = 1
    be = -1
    for e, c in sorted(counter.items()):
        if e-be > 1:
            print(0)
            return
        if e == 0 and c > 1:
            print(0)
            return
        ans *= pow(bef, c)
        ans %= 998244353
        cnt += c
        # print(be, e, c, pow(bef, c))
        be = e
        bef = c
    print(ans)





if __name__ == '__main__':
    main()
