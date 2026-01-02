#!/usr/bin/env python
# coding: utf-8

def readInt():
    return int(input())

def readList():
    return list(input().split())

def readListI():
    return list(map(int, input().split()))

def pattern(n):
    ret = []
    for i in range(pow(2, n)):
        p = [0 for _ in range(n)]
        for j in range(n):
            if (i >> j) & 1:
                p[j] = 1
        ret.append(p)
    return ret

def main():
    n, m = readListI()
    lk = []
    lls = []
    for _ in range(m):
        d = readListI()
        k = d[0]
        ls = [s-1 for s in d[1:]]
        lk.append(k)
        lls.append(ls)
    lp = readListI()
    ret = 0
    for p in pattern(n):
        ok = True
        for i, ls in enumerate(lls):
            if sum(p[s] for s in ls) % 2 != lp[i]:
                ok = False
                break
        if ok:
            ret += 1
    print(ret)


if __name__ == '__main__':
    main()
