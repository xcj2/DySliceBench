p, g = 998244353, 3
invg = pow(g, p-2, p)
W = [pow(g, (p - 1) >> i, p) for i in range(24)]
iW = [pow(invg, (p - 1) >> i, p) for i in range(24)]

def fft(k, f):
    for l in range(k)[::-1]:
        d = 1 << l
        u = 1
        for i in range(d):
            for j in range(i, 1 << k, 2*d):
                f[j], f[j+d] = (f[j] + f[j+d]) % p, u * (f[j] - f[j+d]) % p
            u = u * W[l+1] % p

def ifft(k, f):
    for l in range(k):
        d = 1 << l
        u = 1
        for i in range(d):
            for j in range(i, 1 << k, 2*d):
                f[j+d] *= u
                f[j], f[j+d] = (f[j] + f[j+d]) % p, (f[j] - f[j+d]) % p
            u = u * iW[l+1] % p

def convolve(a, b):
    n0 = len(a) + len(b) - 1
    k = (n0).bit_length() + 1
    n = 1 << k
    a = a + [0] * (n - len(a))
    b = b + [0] * (n - len(b))
    fft(k, a), fft(k, b)
    for i in range(n):
        a[i] = a[i] * b[i] % p
    ifft(k, a)
    invn = pow(n, p - 2, p)
    for i in range(n0):
        a[i] = a[i] * invn % p
    return a[:n0]

N, M = map(int, input().split())
A = [int(a) for a in input().split()]
B = [int(a) for a in input().split()]
print(*convolve(A, B))
