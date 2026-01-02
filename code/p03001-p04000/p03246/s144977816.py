#!/usr/bin/env python3

def main():
    n = int(input())
    vn = list(map(int, input().split()))
    even = count(vn, n, True)
    odd = count(vn, n, False)
    e1k, e1v, e2k, e2v = largest(even)
    o1k, o1v, o2k, o2v = largest(odd)
    res = solve(e1k, e1v, e2k, e2v, o1k, o1v, o2k, o2v, n)
    print(res)

def solve(e1k, e1v, e2k, e2v, o1k, o1v, o2k, o2v, n):
    if e1k != o1k:
        return n - e1v - o1v
    return min(n - e1v - o2v, n - e2v - o1v)

def count(vn, n, is_even):
    di = {}
    st = 0 if is_even else 1
    for i in range(st, n, 2):
        v = vn[i]
        if v in di:
            di[v] += 1
        else:
            di[v] = 1
    return di

def largest(di):
    li_tu = []
    for k in di:
        tu = (k, di[k])
        li_tu.append(tu)
    li_tu = sorted(li_tu, reverse=True, key=lambda x: x[1])
    assert len(li_tu) >= 1
    lg_key = li_tu[0][0]
    lg_val = li_tu[0][1]
    if len(li_tu) == 1:
        sc_key = 0
        sc_val = 0
    else:
        sc_key = li_tu[1][0]
        sc_val = li_tu[1][1]
    return lg_key, lg_val, sc_key, sc_val

main()
