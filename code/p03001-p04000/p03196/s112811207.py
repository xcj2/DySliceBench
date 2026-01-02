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


# 入力:整数n      ex)100
# 出力:約数リスト ex)[1, 5, 25, 2, 10, 50, 4, 20, 100]
def divisorEnumulation(n):
    divisor = []
    for div in divisorize(factorize(n)):
        divisor.append(num(div))
    return divisor


# 使用例
# print(divisorEnumulation(100))

n, p = [int(i) for i in input().split()]
fact = factorize(p)
out = 1
for i in range(len(fact)):
    out *= fact[i][0] ** (fact[i][1]//n)
print(out)
