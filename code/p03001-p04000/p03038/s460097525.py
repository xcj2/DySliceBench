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
    la = rli()
    lcb = []
    for _ in range(m):
        b, c = rli()
        lcb.append((c, b))
    la.sort()
    lcb.sort(reverse=True)
    a_id = 0
    cb_id = 0
    ans = 0
    flag = False
    while a_id < len(la) and cb_id < len(lcb):
        b = lcb[cb_id][1]
        c = lcb[cb_id][0]
        for i in range(b):
            if a_id >= len(la):
                flag = True
                break
            a = la[a_id]
            if a >= c:
                flag = True
                break
            ans += c
            a_id += 1
        if flag:
            break
        cb_id += 1
    ans += sum(la[a_id:])

    print(ans)


if __name__ == '__main__':
    main()
