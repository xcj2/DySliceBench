#!/usr/bin/env python
# coding: utf-8

def readInt():
    return int(input())

def readList():
    return list(input().split())

def readListI():
    return list(map(int, input().split()))

def main():
    n, k = readListI()
    lv = readListI()
    ret = 0
    for l in range(min(n, k)+1):
        for r in range(min(n, k)+1-l):
            jewel = sorted(lv[:l] + lv[n-r:])
            for p in range(l+r):
                if l+r+p > k:
                    continue
                ret = max(ret, sum(jewel[p:]))
    print(ret)


if __name__ == '__main__':
    main()
