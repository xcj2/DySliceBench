# -*- coding: utf-8 -*-
"""
C - 755
TLE
"""
def gen_357():
    def conv(n):
        res = []
        while n:
            n, r = divmod(n, 4)
            if r == 0 and n:
                return '0'
            res.append(str(str(r)))
        if not res:
            res = ['0']
        return ''.join(res[::-1]).translate(str.maketrans('0123', '0357'))

    n = 0
    while True:
        t = conv(n)
        while '0' in t or len(set(list(t))) != 3:
            n += 1
            t = conv(n)
        yield t
        n += 1


def solve(n):
    ans = 0
    g = gen_357()
    while True:
        t = next(g)
        if int(t) > n:
            break
        ans += 1
    return ans


n = int(input())
ans = solve(n)
print(ans)
