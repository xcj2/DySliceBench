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
    ls = Counter()
    for i in range(n):
        s = input()
        ls[s] += 1
    m = -1
    ans = []
    for k, c in ls.most_common():
        if m == -1:
            m = c
        if c < m:
            break
        ans.append(k)
    ans.sort()
    for s in ans:
        print(s)


if __name__ == '__main__':
    main()
