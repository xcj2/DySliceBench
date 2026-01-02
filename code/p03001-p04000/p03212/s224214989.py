N = int(input())


def resol_a(x, a):
    if x < 10:
        return int(x >= a)
    d = 0
    while x > 10**(d+1):
        d += 1
    f = x // 10 ** d
    r = x % 10 ** d
    c = resol_a(r, a)
    b = resol_a(10 ** d - 1, a)
    bb = resol_a(10 ** (d - 1), a)
    if f > a:
        return b + 1
    elif f == a:
        return b + c - bb
    else:
        return b


def resol_ab(x, a, b):
    d = 0
    if x < 100:
        return (x >= 10 * b + a) + (x >= 10 * a + b)
    while x > 10 ** (d + 1):
        d += 1
    f = x // 10 ** d
    r = x % 10 ** d
    if f > a:
        return resol_ab((a+1)*10**d-1, a, b)
    elif f == a:
        return resol_ab(a * 10 ** d - 1, a, b) + max(resol_ab(r, a, b) - resol_ab(10 **
                                                                                  (d - 1), a, b), 0) + max(resol_a(r, b) - resol_a(10 ** (d - 1), b), 0)
    elif f > b:
        return resol_ab((b+1)*10 ** d - 1, a, b)
    elif f == b:
        return resol_ab(b * 10 ** d - 1, a, b) + max(resol_ab(r, a, b) - resol_ab(10 **
                                                                                  (d - 1), a, b), 0) + max(resol_a(r, a) - resol_a(10 ** (d - 1), a), 0)
    else:
        return resol_ab(10 ** d - 1, a, b)


def resol_abc(x, a, b, c):
    if x < 1000:
        A, B, C = str(a), str(b), str(c)
        return sum([x >= int(_) for _ in [A+B+C, A+C+B, B+A+C, B+C+A, C+A+B, C+B+A]])
    d = 0
    while x > 10 ** (d + 1):
        d += 1
    f = x // 10 ** d
    r = x % 10 ** d
    if f > a:
        return resol_abc((a+1)*10**d-1, a, b, c)
    elif f == a:
        return resol_abc(a*10**d-1, a, b, c)+max(resol_abc(r, a, b, c)-resol_abc(10**(d-1), a, b, c), 0)+max(resol_ab(r, b, c)-resol_ab(10**(d-1), b, c), 0)
    elif f > b:
        return resol_abc((b+1)*10**d-1, a, b, c)
    elif f == b:
        return resol_abc(b*10**d-1, a, b, c)+max(resol_abc(r, a, b, c)-resol_abc(10**(d-1), a, b, c), 0)+max(resol_ab(r, a, c)-resol_ab(10**(d-1), a, c), 0)
    elif f > c:
        return resol_abc((c+1)*10**d-1, a, b, c)
    elif f == c:
        return resol_abc(c*10**d-1, a, b, c)+max(resol_abc(r, a, b, c)-resol_abc(10**(d-1), a, b, c), 0)+max(resol_ab(r, a, b)-resol_ab(10**(d-1), a, b), 0)
    else:
        return resol_abc(10**d-1, a, b, c)


print(resol_abc(N, 7, 5, 3))