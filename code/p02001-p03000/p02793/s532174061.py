# E - Flatten

n = int(input())
a = list(map(int, input().split()))
assert len(a) == n

modulus = 10 ** 9 + 7
binmod = (bin(modulus - 2))[2:]  # modulus - 2 in binary

MAX = 10 ** 6

primefact = [0 for i in range(MAX + 1)]

def sieve():
    # cf. https://www.geeksforgeeks.org/lcm-of-n-numbers-modulo-m/
    for i in range(2, MAX + 1):
        if primefact[i] == 0:
            for j in range(i, MAX + 1, i):
                if primefact[j] == 0:
                    primefact[j] = i

def factorize(x):
    if primefact[2] == 0:
        sieve()

    vec = {}
    while x >= 2:
        d = primefact[x]
        if d not in vec:
            vec[d] = 0
        vec[d] += 1
        x //= d
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

fact = [factorize(x) for x in a]

fset = set()
for f in fact:
    fset.update(f.keys())

l = {k: 0 for k in fset}
for f in fact:
    for k in f:
        l[k] = max(l[k], f[k])
lcm = value(l)

s = sum(div(lcm, x) for x in a) % modulus
print(s)
