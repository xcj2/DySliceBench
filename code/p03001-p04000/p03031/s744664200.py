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
    switch = []
    for i in range(m):
        tmp = rli()
        k = tmp[0]
        ls = tmp[1:]
        switch.append(ls)
    lp = rli()
    ans = 0
    def check(mask):
        on_off = []
        for i in range(0, n):
            on_off.append(mask & (1 << i))
        for i in range(m):
            cnt = sum(1 for s in switch[i] if on_off[s-1])
            if cnt % 2 != lp[i]:
                return 0
        return 1
    ans = 0
    for i in range(1 << n):
        ans += check(i)
    print(ans)





if __name__ == '__main__':
    main()
