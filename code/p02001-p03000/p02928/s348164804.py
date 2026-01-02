def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

# mを法とするaの乗法的逆元
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# nCr mod m
# modinvが必要
# rがn/2に近いと非常に重くなる
def combination(n, r, mod=10 ** 9 + 7):
    r = min(r, n - r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i + 1, mod) % mod
    return res

n, k = map(int, input().split())
dat = list(map(int, input().split()))
datAfter = [0] * n
datSelf = [0] * n
numAfter = 0
numSelf = 0
m = 10**9 + 7
for i in range(n):
    for j in range(i+1, n):
        if dat[i] > dat[j]:
            numAfter += 1
for i in range(n):
    for j in range(n):
        #print(dat[i], dat[j])
        if dat[i] > dat[j]:
            numSelf += 1
res = 0
res += numAfter * k
res += numSelf * combination(k, 2)
res %= m
#print(numSelf, numAfter, res)
print(res)