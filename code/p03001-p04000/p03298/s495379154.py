from collections import defaultdict
from itertools import combinations


def get_pair(s, cmb):
    g, h = 0, 0
    for i in range(n):
        if i in cmb:
            g <<= 5
            g += s[i]
        else:
            h <<= 5
            h += s[i]
    return g, h


def patterns(k, d, e):
    ret = 0
    f = defaultdict(int)
    for cmb in combinations(range(n), k):
        f[get_pair(d, cmb)] += 1
    for cmb in combinations(range(n), k):
        ret += f[get_pair(e, cmb)]
    return ret


def solve(n, b):
    d = b[:n]
    e = b[2 * n - 1:n - 1:-1]
    ans = 0

    if n % 2 == 0:
        for k in range(n // 2):
            ans += 2 * patterns(k, d, e)
        ans += patterns(n // 2, d, e)
    else:
        for k in range(n // 2 + 1):
            ans += 2 * patterns(k, d, e)
    return ans


n = int(input())
s = input()
a = ord('a') - 1
b = [ord(c) - a for c in s]
print(solve(n, b))
