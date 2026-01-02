def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

N = int(input())
N *= 2

def crt(a, n, b, m, inv):
    out = a
    #inv = pow(n, -1, m)
    out += (b - a) * n * inv
    return out % (n * m)

p = []

i = 2
while i * i <= N:
    curr = 1
    while N % i == 0:
        N//= i
        curr *= i
    if curr != 1:
        p.append(curr)
    i += 1
    
if N != 1:
    p.append(N)

poss = [0]
mod = 1
for v in p:
    new = []
    #inv = pow(mod, -1, v)
    inv = modinv(mod, v)
    for u in poss:
        new.append(crt(u, mod, 0, v, inv))
        new.append(crt(u, mod, -1, v, inv))
    poss = new
    mod *= v
poss.sort()
poss += [mod]
print(poss[1])