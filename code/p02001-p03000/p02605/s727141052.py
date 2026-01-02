import sys
readline = sys.stdin.readline


def solve():
    N = int(readline())
    X = [0] * N
    Y = [0] * N
    U = [0] * N

    for i in range(N):
        x, y, u = readline().split()
        X[i] = int(x)
        Y[i] = int(y)
        U[i] = u
    
    ans = 10 ** 10

    _U,D,L,R = 'U','D','L','R'

    rs = [(X[i], Y[i]) for i in range(N) if U[i] == R]
    ls = [(X[i], Y[i]) for i in range(N) if U[i] == L]
    ans = min(ans, horizon(rs, ls))

    rs = [(Y[i], X[i]) for i in range(N) if U[i] == _U]
    ls = [(Y[i], X[i]) for i in range(N) if U[i] == D]
    ans = min(ans, horizon(rs, ls))


    # cross
    rs = [(X[i], Y[i]) for i in range(N) if U[i] == R]
    ds = [(X[i], Y[i]) for i in range(N) if U[i] == D]
    ans = min(ans, cross(rs, ds))

    rs = [(X[i], -Y[i]) for i in range(N) if U[i] == R]
    ds = [(X[i], -Y[i]) for i in range(N) if U[i] == _U]
    ans = min(ans, cross(rs, ds))

    rs = [(-X[i], Y[i]) for i in range(N) if U[i] == L]
    ds = [(-X[i], Y[i]) for i in range(N) if U[i] == D]
    ans = min(ans, cross(rs, ds))

    rs = [(-X[i], -Y[i]) for i in range(N) if U[i] == L]
    ds = [(-X[i], -Y[i]) for i in range(N) if U[i] == _U]
    ans = min(ans, cross(rs, ds))

    if ans == 10 ** 10:
        print('SAFE')
    else:
        print(ans)


def horizon(rights, lefts):
    Y = {}
    for rx, ry in rights:
        if ry not in Y:
            Y[ry] = []
        Y[ry].append(rx)
    for k in Y:
        Y[k].sort()

    res = 10 ** 10
    
    for lx, ly in lefts:
        if ly not in Y:
            continue
        xs = Y[ly]
        t = bisect_right(xs, lx)
        if t == -1:
            continue
        else:
            res = min(res, (lx - xs[t]) * 5)
    
    return res

def bisect_right(xs, x):
    l, r = -1, len(xs)
    while l + 1 < r:
        m = (l + r) // 2
        if xs[m] < x:
            l = m
        else:
            r = m
    return l

def cross(rights, downs):
    x_seps = {}
    
    for x, y in rights:
        xsep = x - y
        if xsep not in x_seps:
            x_seps[xsep] = []
        
        x_seps[xsep].append(x)
    
    for k in x_seps:
        x_seps[k].sort()
    
    res = 10 ** 10

    for x, y in downs:
        xsep = x - y
        if xsep not in x_seps:
            continue
        xs = x_seps[xsep]
        t = bisect_right(xs, x)
        if t != -1:
            res = min(res, (x - xs[t]) * 10)

    return res

solve()