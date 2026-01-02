p, g = 998244353, 3
invg = pow(g, p-2, p)
W = [pow(g, (p - 1) >> i, p) for i in range(24)]
iW = [pow(invg, (p - 1) >> i, p) for i in range(24)]
def convolve(a, b):
    def fft(f):
        for l in range(k)[::-1]:
            d = 1 << l
            v = W[l+1]
            u = 1
            for i in range(d):
                for j in range(i, n, 2*d):
                    f[j], f[j+d] = (f[j] + f[j+d]) % p, u * (f[j] - f[j+d]) % p
                u = u * v % p

    def ifft(f):
        for l in range(k):
            d = 1 << l
            v = iW[l+1]
            u = 1
            for i in range(d):
                for j in range(i, n, 2*d):
                    f[j+d] *= u
                    f[j], f[j+d] = (f[j] + f[j+d]) % p, (f[j] - f[j+d]) % p
                u = u * v % p

    n0, n1 = len(a), len(b)
    k = (max(n0, n1) - 1).bit_length() + 1
    n = 1 << k
    a = a + [0] * (n-n0)
    b = b + [0] * (n-n1)
    fft(a), fft(b)
    for i in range(n):
        a[i] = a[i] * b[i] % p
    ifft(a)
    invn = pow(n, p - 2, p)
    return [a[i] * invn % p for i in range(n0 + n1 - 1)]

N, M = map(int, input().split())
A = [int(a) for a in input().split()]
B = [int(a) for a in input().split()]
print(*convolve(A, B))
