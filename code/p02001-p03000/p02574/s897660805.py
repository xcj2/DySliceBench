def f1(n):
    max_p = int(n ** 0.5)
    p = 0  # 素数
    pl = []  # 素数リスト
    el = [i for i in range(2, n + 1)]  # 探索リスト
    D = [i for i in range(n + 1)]
    while p <= max_p:
        nxt = []
        p = el[0]
        pl.append(p)
        for e in el:
            if e % p == 0:
                D[e] = p
            else:
                nxt.append(e)
        el = nxt
    for e in el:
        D[e] = e
    pl.extend(el)
    return D, pl


def f2(n, D):
    s = set()
    x = n
    while x > 1:
        p = D[x]
        s.add(p)
        x = x // p
    return s


from math import gcd


def is_nc(n, al):
    g = al[0]
    for i, a in enumerate(al):
        if i == 0:
            continue
        else:
            g = gcd(g, a)
            if g == 1:
                return False
    return True


def is_sc(n, al):
    max_al = max(al)
    if max_al == 1:
        return False
    D, pl = f1(max_al)
    count = {p: 0 for p in pl}
    for a in al:
        p_s = f2(a, D)
        for p in p_s:
            if count[p] == 1:
                return True
            else:
                count[p] += 1
    return False


n = int(input())
al = list(map(int, input().split()))
if is_nc(n, al):
    print('not coprime')
elif is_sc(n, al):
    print('setwise coprime')
else:
    print('pairwise coprime')