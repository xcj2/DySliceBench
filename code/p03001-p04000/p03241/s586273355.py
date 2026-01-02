


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


x,n = map(int,input().split())
if x == 1 and n == 1:
    print(1)
    exit()
fct = factorize(n)


divlist=[]
for div in divisorize(fct):
    divlist.append(num(div))

divlist.sort()
ans = 1
for i in range(0,len(divlist)):
    if divlist[i] <= n/x:
        ans = divlist[i]
print(ans)