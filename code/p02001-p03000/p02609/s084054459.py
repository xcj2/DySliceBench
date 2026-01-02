import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = int(readline())
lst1 = list(readline().rstrip().decode('utf-8'))


res = lst1.copy()
res = "".join(res)
ct = res.count("1")
res = int(res,2)
if ct == 0:
    for i in range(n):
        print(1)
    exit()
if ct == 1:
    amari_of_m = -1
else:
    amari_of_m = res%(ct-1)
amari_of_p = res%(ct+1)

def pow(n,p,mod): #繰り返し二乗法(nのp乗)
    res = 1
    while p > 0:
        if p % 2 == 0:
            n = n ** 2 % mod
            p //= 2
        else:
            res = res * n % mod
            p -= 1
    return res % mod

def func(res):
    ans = 1
    while True:
        ct = 0
        for i in range(len(bin(res))):
            if res>>i&1:
                ct += 1
        if res%ct == 0:
            print(ans+1)
            return
        else:
            res %= ct
            ans += 1

for i in range(n):
    if lst1[i] == "1" and amari_of_m == -1:
        print(0)
        continue
    else:
        resres = pow(2,n-i-1,ct-1) if lst1[i] == "1" else pow(2,n-i-1,ct+1)
    if lst1[i] == "1":
        resres = amari_of_m - resres
        resres %= ct-1
    else:
        resres = amari_of_p + resres
        resres %= ct+1
    if not resres:
        print(1)
    else:
        func(resres)
