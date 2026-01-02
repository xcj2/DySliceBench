def factors(n):
    res = {}
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            res[i] = 0
            while n % i == 0:
                res[i] += 1
                n //= i
    if n > 1: res[n] = 1
    return res

def sel2(f, a, b):
    g = [(k, v) for k, v in f.items() if v >= a]
    res = 0
    for ik, iv in g:
        for jk, jv in g:
            if ik == jk: continue
            if jv < b: continue
            res += 1
    return res

def sel3(f, a, b, c):
    g = [(k, v) for k, v in f.items() if v >= a]
    res = 0
    for ik, iv in g:
        for jk, jv in g:
            if ik == jk: continue
            if jv < b: continue
            for kk, kv in g:
                if kk in (ik, jk): continue
                if kk < jk: continue
                if kv < c: continue
                res += 1
    return res

n = int(input())
facs = {}
for i in range(2, n+1):
    tmp = factors(i)
    for k, v in tmp.items():
        if k in facs: facs[k] += v
        else: facs[k] = v

res = 0
res += sum(1 for k, v in facs.items() if v >= 74)
res += sel2(facs, 2, 24)
res += sel2(facs, 4, 14)
res += sel3(facs, 2, 4, 4)
print(res)