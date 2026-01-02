# coding: utf-8

import sys
input = sys.stdin.readline

def f4(n, h, a):
    bit = [0] * (n + 1)

    def getmax(h):
        x = h - 1
        m = 0
        while x != 0:
            if m < bit[x]:
                m = bit[x]
            x -= x & -x
        return(m)

    def update(h, v):
        x = h
        while x <= n:
            if bit[x] < v:
                bit[x] = v
            x += x & -x

    for i in range(1, n + 1):
        m = getmax(h[i])
        update(h[i], m + a[i])
    return(max(bit))

n = int(input()) # 1 <= n <= 2 x 10^5
h = [0] + list(map(int, input().split()))
a = [0] + list(map(int, input().split()))

print(f4(n, h, a))
