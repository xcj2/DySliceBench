#!/usr/bin/env python
# coding: utf-8

import heapq

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

def main():
    n, m = rli()
    ll = []
    for _ in range(n):
        a, b = rli()
        ll.append((a, b))
    ll.sort()
    pq = []
    l = 0
    ans = 0
    for i in range(1, m+1):
        while l < len(ll) and ll[l][0] <= i:
            heapq.heappush(pq, -ll[l][1])
            l += 1
        if len(pq) > 0:
            ans -= heapq.heappop(pq)
    print(ans)


if __name__ == '__main__':
    main()
