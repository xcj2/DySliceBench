# E - Flatten

n = int(input())
a = list(map(int, input().split()))
assert len(a) == n

modulus = 10 ** 9 + 7
binmod = (bin(modulus - 2))[2:]  # modulus - 2 in binary

MAX = 10 ** 6

def factorize(x):
    vec = {}
    d = 2
    while d * d <= x:
        if x % d == 0:
            if d not in vec:
                vec[d] = 0
            vec[d] += 1
            x //= d
        else:
            d += 1
    if x > 1:
        if x not in vec:
            vec[x] = 0
        vec[x] += 1
    return vec

def value(x):
    p = 1
    for i in x:
        p = (p * (i ** x[i])) % modulus
    return p

def inverse(x):
    p = 1
    for b in binmod:
        p = p * p % modulus
        if b == '1':
            p = p * x % modulus
    return p

def div(n, d):
    return n * inverse(d) % modulus

l = {}
for x in a:
    f = factorize(x)
    for k in f:
        l[k] = max(l[k], f[k]) if k in l else f[k]
lcm = value(l)

s = sum(div(lcm, x) for x in a) % modulus
print(s)
