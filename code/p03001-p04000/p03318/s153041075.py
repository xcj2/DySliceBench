def nsn(n):
    s = 0
    nn = n
    while nn > 0:
        s += nn % 10
        nn = int(nn / 10)
    return n / s

def big(a):
    r = 1
    while a > 0:
        r *= 10
        a = int(a / 10)
    return r

def clear(a, d):
    aa = a
    asa = nsn(a)
    b = True
    ba = big(a)
    while aa < ba:
        aa += d
        if nsn(aa) < asa:
            b = False
            break
    return b

K = int(input())
T = [1]
a = 1
d = 1
while len(T) < K:
    n = 1
    while 1:
        an = a + n * d
        if clear(an, d):
            T.append(an)
            a = an
            d = n * d
            break
        n += 1
for x in T:
    print(x)