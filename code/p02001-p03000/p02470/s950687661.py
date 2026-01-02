def factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def factorize2(n):
    plist = factorize(n)
    dic = {}
    for n in plist:
        if not n in dic:
            dic[n] = 1
        else:
            dic[n] += 1
    ret = []
    for p,n in dic.items():
        ret.append([p,n])
    return ret

def phi(n):
    plist = factorize2(n)
    ans = 1
    for [p,n] in plist:
        ans *= (pow(p,n)-pow(p,n-1))
    return ans

Q = int(input())
print(phi(Q))

