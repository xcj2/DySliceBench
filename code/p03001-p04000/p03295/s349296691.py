#!/usr/bin/env python
# coding: utf-8

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

def main():
    n, m = rli()
    edges = []
    for _ in range(m):
        a, b = rli()
        edges.append((a, b))
    edges.sort(key=lambda x:x[1])
    ans = 0
    left = 0
    for e in edges:
        if e[0] <= left:
            continue
        ans += 1
        left = e[1]-1
    #     print(ans, e[0], left)
    # print(edges)
    print(ans)


if __name__ == '__main__':
    main()
