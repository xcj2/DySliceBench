def convolve(a, b):
    def fft():
        d = n // 2
        v1 = w1
        v2 = w2
        v3 = w3
        while d >= 1:
            u1 = 1
            u2 = 1
            u3 = 1
            for i in range(d):
                for j in range(i, n, 2*d):
                    f1[j], f1[j+d] = (f1[j] + f1[j+d]) % p1, u1 * (f1[j] - f1[j+d]) % p1
                    f2[j], f2[j+d] = (f2[j] + f2[j+d]) % p2, u2 * (f2[j] - f2[j+d]) % p2
                    f3[j], f3[j+d] = (f3[j] + f3[j+d]) % p3, u3 * (f3[j] - f3[j+d]) % p3
                    g1[j], g1[j+d] = (g1[j] + g1[j+d]) % p1, u1 * (g1[j] - g1[j+d]) % p1
                    g2[j], g2[j+d] = (g2[j] + g2[j+d]) % p2, u2 * (g2[j] - g2[j+d]) % p2
                    g3[j], g3[j+d] = (g3[j] + g3[j+d]) % p3, u3 * (g3[j] - g3[j+d]) % p3
                u1 = u1 * v1 % p1
                u2 = u2 * v2 % p2
                u3 = u3 * v3 % p3
            v1 = v1 * v1 % p1
            v2 = v2 * v2 % p2
            v3 = v3 * v3 % p3
            d //= 2
 
    def ifft():
        d = 1
        while d < n:
            v1 = pow(invw1, n // (2 * d), p1)
            v2 = pow(invw2, n // (2 * d), p2)
            v3 = pow(invw3, n // (2 * d), p3)
            u1 = 1
            u2 = 1
            u3 = 1
            for i in range(d):
                for j in range(i, n, 2*d):
                    f1[j+d] *= u1
                    f2[j+d] *= u2
                    f3[j+d] *= u3
                    f1[j], f1[j+d] = (f1[j] + f1[j+d]) % p1, (f1[j] - f1[j+d]) % p1
                    f2[j], f2[j+d] = (f2[j] + f2[j+d]) % p2, (f2[j] - f2[j+d]) % p2
                    f3[j], f3[j+d] = (f3[j] + f3[j+d]) % p3, (f3[j] - f3[j+d]) % p3
                u1 = u1 * v1 % p1
                u2 = u2 * v2 % p2
                u3 = u3 * v3 % p3
            d *= 2
 
    p1, g1 = (11 << 21) + 1, 3
    p2, g2 = (25 << 20) + 1, 3
    p3, g3 = (27 << 20) + 1, 5
    
    n0, n1 = len(a), len(b)
    n = 1 << (max(n0, n1) - 1).bit_length() + 1
    a = a + [0] * (n-n0)
    b = b + [0] * (n-n1)
    w1 = pow(g1, (p1 - 1) // n, p1)
    w2 = pow(g2, (p2 - 1) // n, p2)
    w3 = pow(g3, (p3 - 1) // n, p3)
    invw1 = pow(w1, p1-2, p1)
    invw2 = pow(w2, p2-2, p2)
    invw3 = pow(w3, p3-2, p3)
    
    f1 = [aa % p1 for aa in a]
    f2 = [aa % p2 for aa in a]
    f3 = [aa % p3 for aa in a]
    
    g1 = [aa % p1 for aa in b]
    g2 = [aa % p2 for aa in b]
    g3 = [aa % p3 for aa in b]
    
    fft()
    for i in range(n):
        f1[i] = f1[i] * g1[i] % p1
        f2[i] = f2[i] * g2[i] % p2
        f3[i] = f3[i] * g3[i] % p3
    ifft()
    invn1 = pow(n, p1 - 2, p1)
    invn2 = pow(n, p2 - 2, p2)
    invn3 = pow(n, p3 - 2, p3)
    k1 = pow(n * p2 * p3 % p1, p1-2, p1) * p2 * p3
    k2 = pow(n * p1 * p3 % p2, p2-2, p2) * p1 * p3
    k3 = pow(n * p1 * p2 % p3, p3-2, p3) * p1 * p2
    q = p1 * p2 * p3
    return [(f1[i] * k1 + f2[i] * k2 + f3[i] * k3) % q % P for i in range(n0 + n1 - 1)]

def grow(d, v, h):
    h += [0] * d
    f = [(-1 if (i+d) % 2 else 1) * fainv[i] * fainv[d-i] % P * h[i] % P for i in range(d+1)]
    
    for idx, a in enumerate([d+1, d * fa[v-1] * fainv[v] % P, (d * fa[v-1] * fainv[v] + d + 1) % P]):
        g = [pow(a - d + i - 1, P-2, P) if i else 0 for i in range(2*d+2)]
        fg = convolve(f, g)
        p = 1
        for i in range(d+1):
            p = p * (a-i) % P
        for i in range(d+1):
            fg[d+i+1] = fg[d+i+1] * p % P
            p = p * (a+i+1) % P * pow(a-d+i, P-2, P) % P
        if idx == 1:
            for i in range(d+1):
                h[i] = h[i] * fg[d+i+1] % P
        elif idx == 0:
            for i in range(d):
                h[i+d+1] = fg[d+i+1]
        elif idx == 2:
            for i in range(d):
                h[i+d+1] = h[i+d+1] * fg[d+i+1] % P
    return h

# Create a table of the factorial of the first v+2 multiples of v, i.e., [0!, v!, 2v!, ..., (v(v+1))!]
def create_table(v):
    s = 1
    X = [1, v+1]
    while s < v:
        X = grow(s, v, X)
        s *= 2
    table = [1]
    for x in X:
        table.append(table[-1] * x % P)
    return table

def fact(i, table):
    a = table[i//v]
    for j in range(i//v*v+1, i+1):
        a = a * j % P
    return a

P = 10**9+7
v = 1 << 11
fa = [1] * (2*v+2)
fainv = [1] * (2*v+2)
for i in range(2*v+1):
    fa[i+1] = fa[i] * (i+1) % P
fainv[-1] = pow(fa[-1], P-2, P)
for i in range(2*v+1)[::-1]:
    fainv[i] = fainv[i+1] * (i+1) % P

T = create_table(v)

f = lambda a, b: fact(a+b+2, T) * pow(fact(a+1, T) * fact(b+1, T), P-2, P) % P
r1, c1, r2, c2 = map(int, input().split())
print((f(r2, c2) - f(r2, c1-1) - f(r1-1, c2) + f(r1-1, c1-1)) % P)