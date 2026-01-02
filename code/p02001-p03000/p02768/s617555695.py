M,A,B = [int(x) for x in input().split()]

mod = 10**9+7

def cmb(n, r, mod):
    r = min(r, n-r)
    res = 1
    for i in range(r):
        res = res * (n - i) % mod * pow(i+1, mod-2, mod) % mod
    return res

def binary(n):
    return bin(n)[2:]


def pow_by_binary_exponentiation(a, x, n): # a^x mod n
    x = [int(b) for b in binary(x)]
    y = a
    for i in range(1, len(x)):
        y = (y**2) % n
        if x[i] == 1:
            y = (y * a) % n
    return y
d = pow_by_binary_exponentiation(2,M,mod)-1
    
d1 = cmb(M,A,mod)
d2 = cmb(M,B,mod)
print((d-d1-d2)%mod)