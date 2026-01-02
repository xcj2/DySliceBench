def isprime(n):
    if(n<2):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True

def primelist(n):
    return [i for i in range(n) if isprime(i)]

def factor(n):
    f = {}
    while(n > 1):
        for p in primelist(n+1):
            if(n % p == 0):
                f[p] = f.get(p, 0) + 1
                n //= p
    return f

def factorfactorial(n):
    f = {}
    for i in range(1,n+1):
        fi = factor(i)
        for k, v in fi.items():
            f[k] = f.get(k,0) + v
    return f

# 75 = 3*5*5 = 3*25 = 5*15 
n = int(input())
f = factorfactorial(n)

# print(f)
cnt = 0

for i in f.keys():
    if(f[i]>=75-1):
        cnt += 1
    for j in primelist(n+1):
        if(i==j):
            continue
        if(f[i]>=25-1 and f[j]>=3-1):
            cnt += 1
        if(f[i]>=15-1 and f[j]>=5-1):
            cnt += 1
        if(i > j):
            for k in primelist(n+1):
                if k in [i,j]:
                    continue
                if(f[i]>=5-1 and f[j]>=5-1 and f[k]>=3-1):
                    cnt += 1



print(cnt)
