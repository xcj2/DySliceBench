N = int(input())
A = map(int, input().split())

def factorize(x):
    """xの素因数分解を表す辞書 {素因数: 指数}"""
    f = {}
    d = 2
    while x > 1:
        c = 0
        while x % d == 0:
            c += 1
            x //= d
        if c > 0:
            f[d] = c
        d += 1 if d == 2 else 2
        if d * d > x > d:
            f[x] = 1
            break
    return f

def factorizeWithSet(x, D):
    f = {}
    for d in D:
        c = 0
        while x % d == 0:
            c += 1
            x //= d
        if c > 0:
            f[d] = c
    return f

def dropmin(ls):
    """[min(ls[:i] + ls[i + 1:]) for i in range(len(ls))]"""
    # l = [min(ls[:i]) for i in range(len(ls))]
    l = [float('inf')] * N
    for i in range(1, N):
        l[i] = min(l[i - 1], ls[i - 1])
    # r = [min(ls[i + 1:]) for i in range(len(ls))]
    r = [float('inf')] * N
    for i in range(N - 2, -1, -1):
        r[i] = min(r[i + 1], ls[i + 1])
    return [min(a, b) for a, b in zip(l, r)]

def prod(ls):
    p = 1
    for x in ls:
        p *= x
    return p

# 各A_iの素因数
A = list(A)
F = [factorize(a) for a in A[:2]]

# 素因数の集合 (2要素に出現しない素因数は無視)
D =  set(F[0].keys())
D.update(F[1].keys())

E = set()
for d in D:
    c = 0
    for a in A:
        if a % d != 0:
            c += 1
            if c >= 2:
                E.add(d)
                break
D -= E

F = [factorizeWithSet(a, D) for a in A]

# Dの要素 d -> i -> dがA_iに含まれる個数
X = {d: [f[d] if d in f else 0 for f in F] for d in D}

# Dの要素 d → A_iを削除したときのdの個数の最小値のリスト
X = {d: dropmin(X[d]) for d in D}

S = [prod(d ** X[d][i] for d in D) for i in range(N)]
print(max(S))
