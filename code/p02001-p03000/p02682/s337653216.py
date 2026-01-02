# from numba import njit
 
# @njit(cache=True)
def convolve(a, b):
    def poww(aa, bb, mm):
        ss = 1
        tt = aa
        while bb:
            if bb % 2:
                ss = ss * tt % mm
                bb -= 1
            tt = tt * tt % mm
            bb //= 2
        return ss
    def fft(n, p, g, w, invw, f):
        d = n // 2
        v = w
        while d >= 1:
            u = 1
            for i in range(d):
                for j in range(i, n, 2*d):
                    f[j], f[j+d] = (f[j] + f[j+d]) % p, u * (f[j] - f[j+d]) % p
                u = u * v % p
            v = v * v % p
            d //= 2
 
    def ifft(n, p, g, w, invw, f):
        d = 1
        while d < n:
            v = poww(invw, n // (2 * d), p)
            u = 1
            for i in range(d):
                for j in range(i, n, 2*d):
                    f[j+d] *= u
                    f[j], f[j+d] = (f[j] + f[j+d]) % p, (f[j] - f[j+d]) % p
                u = u * v % p
            d *= 2
 
    p = 1107296257
    g = 5
    n0, n1 = len(a), len(b)
    n = 1
    while n < max(n0, n1) * 2:
        n *= 2
    a = a + [0] * (n-n0)
    b = b + [0] * (n-n1)

    w = poww(g, (p - 1) // n, p)
    invw = poww(w, p-2, p)
    fft(n, p, g, w, invw, a), fft(n, p, g, w, invw, b)
    for i in range(n):
        a[i] = a[i] * b[i] % p
    ifft(n, p, g, w, invw, a)
    invn = poww(n, p - 2, p)
    for i in range(n0 + n1 - 1):
        a[i] = a[i] * invn % p
    return a[:n0 + n1 - 1]

N = 100000
A = []
B = []
s = 0
for i in range(N):
    s = (s * 3 + i * 7) % 100
    a = s
    b = (s * 3 + a * 11) % 100
    A.append(a)
    B.append(b)

AB = convolve(A, B)


#####
A, B, C, K = map(int, input().split())
if K <= A + B:
    print(min(A, K))
else:
    print(A - (K - A - B))