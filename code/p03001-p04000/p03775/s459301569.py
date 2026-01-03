# 入力 : 自然数     ex) 12
# 出力 : 約数リスト ex) [(2,2),(3,1)]
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
        a = a * base ** exponent
    return a

n = int(input())
if n == 1:
    print(1)
    exit()
fct = factorize(n)
maxDigit = n
for div in divisorize(fct):
    outNum = num(div)
    nonOutNum = int(n/outNum)
    digitOut = 0
    digitNonOut = 0
    while outNum > 0:
        digitOut += 1
        outNum = int(outNum / 10)
    while nonOutNum > 0:
        digitNonOut += 1
        nonOutNum = int(nonOutNum / 10)
    if max(digitOut, digitNonOut) < maxDigit:
        maxDigit = max(digitOut, digitNonOut)
print(maxDigit)
