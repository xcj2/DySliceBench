#!/usr/bin/env python3

MOD = 1000000007
fact = []

def main():
    h, w, a, b = map(int, input().split())
    init_fact(200000)
    mp = get_list_middle_points(h, w, a, b)
    res = 0
    for y, x in mp:
        res += count(1, 1, x, y) * count(x, y, w, h)
        res %= MOD
    print(res)

def count(x1, y1, x2, y2):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    count = combi(dx + dy, min(dx, dy))
    return count

def get_list_middle_points(h, w, a, b):
    li = []
    y = h - a
    x = b + 1
    while (y >= 1 and x <= w):
        li.append((y, x))
        y -= 1
        x += 1
    return li

def combi(n, k):
    numera = fact[n]
    denomi = (fact[n - k] * fact[k]) % MOD
    return (numera * inv(denomi)) % MOD

def init_fact(maxn):
    assert len(fact) == 0
    fact.append(1)
    for i in range(1, maxn + 1):
        fact.append((fact[i - 1] * i) % MOD)

def inv(n):
    return pow(n, MOD - 2)

def pow(n, p):
    if p == 0:
        return 1
    elif p % 2 == 0:
        x = pow(n, p // 2)
        return (x * x) % MOD
    else:
        x = pow(n, p - 1)
        return (x * n) % MOD

main()
