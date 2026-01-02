def soin(num):
    re = []
    div = 2
    while 1:
        lim = int(num ** 0.5) + 1
        while num % div:
            div += 1
            if div > lim:
                re += [1]
                return re
        sisu = 0
        while num % div == 0:
            num //= div
            sisu += 1
        re += [sisu]
        if num == 1:
            return re


def com(a, b):
    if a == b:
        return 1
    t = (a, b)
    if (a, b) in com_memo:
        return com_memo[t]
    re = com(a - 1, b) * a // (a - b)
    com_memo[t] = re
    return re


def f(n, m):
    sisus = soin(m)
    ans = 1
    for s in sisus:
        ans = ans * com(s + n - 1, n - 1) % md
    print(ans)


md = 10 ** 9 + 7
n, m = map(int, input().split())
if m==1:
    print(1)
    exit()
com_memo = {}
f(n, m)
