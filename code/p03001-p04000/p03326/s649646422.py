#!/usr/bin/env python
# coding: utf-8

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

def value(c, w):
    return c[0]*w[0]+c[1]*w[1]+c[2]*w[2]

def main():
    n, m = rli()
    cakes = []
    for _ in range(n):
        x, y, z = rli()
        cakes.append((x, y, z))
    ans = 0
    for w in [(1,1,1),(1,1,-1),(1,-1,1),(1,1,-1),(-1,1,1),(-1,1,-1),(-1,-1,1),(-1,-1,-1)]:
        cakes.sort(key=lambda c: value(c,w), reverse=True)
        v = sum(value(c,w) for c in cakes[:m])
        ans = max(ans, v)
        # print(v, cakes)
    print(ans)


if __name__ == '__main__':
    main()
