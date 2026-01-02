def ExtGCD(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = ExtGCD(b, a % b)
        x -= (a // b) * y
        return d, y, x
def ModInv(a, mod):
    return ExtGCD(a, mod)[1] % mod
def ModComb(n, k, mod):
    if n < k or n < 0 or k < 0:
        return 0
    elif n == 0 or k == 0:
        return 1
    q, a = 1, 1
    for i in range(n-k+1, n+1):
        q = (q * i) % mod
    for i in range(2, k+1):
        a = (a * i) % mod
    return int(q * ModInv(a, mod) % mod)
def ModPow(a,n,mod):
    bi=str(format(n,"b"))#2進表現に
    res=1
    for i in range(len(bi)):
        res=(res*res) % mod
        if bi[i]=="1":
            res=(res*a) % mod
    return res
def main():
    n,a,b=map(int,input().split())
    mod=10**9+7
    print((ModPow(2,n,mod) - (ModComb(n,a,mod) + ModComb(n,b,mod))-1)%mod)
main()