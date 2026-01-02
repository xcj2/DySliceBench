import sys
K = int(sys.stdin.readline())

def cands():
    d = 1
    res = []
    res.extend(range(1, 1000))
    for d in range(3, 16):
        y = 10 ** (d-2)
        z = y - 1
        r = map(lambda x: x * y + z, range(100, 1000))
        res.extend(r)
    return res


def S(m):
    res = 0
    while m > 0:
        res += m % 10
        m //= 10
    return res

def is_snuke(i_s_i, m):
    return i_s_i <= m

ss = []
cs = cands()
for i in cs:
    s_i = S(i)
    ss.append((i, s_i, i / s_i))

m = float('inf')
ms = []
for _, _, i_s_i in reversed(ss):
    m = min(m, i_s_i)
    ms.append(m)
ms = list(reversed(ms))

res = 0
for (i, s_i, i_s_i), m in zip(ss, ms):
    b = is_snuke(i_s_i, m)
    if b:
        print(i)
        res += 1
    if K <= res:
        break
