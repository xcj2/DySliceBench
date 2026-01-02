p, g, ig = 998244353, 3, 332748118
W = [pow(g, (p - 1) >> i, p) for i in range(24)]
iW = [pow(ig, (p - 1) >> i, p) for i in range(24)]

def fft(k, f):
    for l in range(k, 0, -1):
        d = 1 << l - 1
        for i in range(1 << k - l):
            u = 1
            for j in range(i * 2 * d, (i * 2 + 1) * d):
                f[j], f[j+d] = (f[j] + f[j+d]) % p, u * (f[j] - f[j+d]) % p
                u = u * W[l] % p

def ifft(k, f):
    for l in range(1, k + 1):
        d = 1 << l - 1
        for i in range(1 << k - l):
            u = 1
            for j in range(i * 2 * d, (i * 2 + 1) * d):
                f[j+d] *= u
                f[j], f[j+d] = (f[j] + f[j+d]) % p, (f[j] - f[j+d]) % p
                u = u * iW[l] % p

def convolve(a, b):
    n0 = len(a) + len(b) - 1
    k = (n0).bit_length()
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
    del a[n0:]
    return a

N, M = map(int, input().split())
A = [int(a) for a in input().split()]
B = [int(a) for a in input().split()]
print(*convolve(A, B))
