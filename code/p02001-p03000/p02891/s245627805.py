#!/usr/bin/env python
# coding: utf-8

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

def change(s, s0=""):
    t = list(s0+s)
    ret = 0
    for i in range(1, len(t)):
        if t[i] == t[i-1]:
            t[i] = '*'
            ret += 1
    return "".join(t[len(s0):]), ret

def main():
    s = input()
    k = ri()
    memo = dict()
    memo2 = []
    bef = ""
    if k < 100:
        _, c = change(s*k, "")
        print(c)
        return
    rep = 0
    for i in range(k):
        ns, c = change(s, bef)
        # print(bef, s, ns, c)
        if ns in memo:
            # print("OK", ns, memo[ns])
            rep = i-memo[ns][1]
            break
        memo[ns] = (c, i)
        memo2.append((c, ns))
        bef = ns
    ans = 0
    for m in memo2:
        ans += m[0]
    assert(len(memo2) < 3)
    rem = k-len(memo2)
    if rep == 1:
        ans += rem*memo2[-rep][0]
    elif rep == 2:
        ans += (rem//2)*sum(m[0] for m in memo2)
        if rem % 2 == 1:
            ans += memo2[0][0]
    print(ans)
    # print(rep, memo, memo2)


if __name__ == '__main__':
    main()
