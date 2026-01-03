#!/usr/bin/env python3

def main():
    n, k = map(int, input().split())
    dk = list(map(int, input().split()))
    assert len(dk) == k

    us = set(usable(dk))
    print(form(us, n))

def form(us, n):
    for res in range(n, 10 ** 5):
        fla = True
        for c in str(res):
            if int(c) not in us:
                fla = False
                break
        if fla:
            return res
    raise Exception

def usable(dk):
    res = []
    for i in range(10):
        if i not in dk:
            res.append(i)
    return res

main()
