
N, P = map(int, input().split())


def factorize(n):
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct


def divisorize(fct):
    b, e = fct.pop()  # base, exponent
    pre_div = divisorize(fct) if fct else [[]]
    suf_div = [[(b, k)] for k in range(e + 1)]
    return [pre + suf for pre in pre_div for suf in suf_div]


def num(fct):
    a = 1
    for base, exponent in fct:
        a = a * base**exponent
    return a


if P==1:
    print(1)
else: 
    fct = factorize(P)
    
    al = []

    for div in divisorize(fct):
        al.append(num(div))

    al.sort()
    al.reverse()

    for i in range(len(al)-1):
        c =0
        tmp = P
        while tmp%al[i] == 0 and al[i]>1:
            c = c+1
            tmp = tmp//al[i]
        if c>=N:
            print(al[i])
            break
    else:
        print(1)
