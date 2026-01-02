mod = 10**6 + 3

fac = [0]*mod
fac[0] = 1
for i in range(1, mod):
    fac[i] = fac[i - 1] * i
    fac[i] %= mod

def gcd(a, b):
    def calc(a, b, first, second):
        if a < b:
            a, b = b, a
        r = a % b
        q = -(a - r)//b
        if r == 0:
            return b, second
        # first += q * second
        first = [x + q * y for (x, y) in zip(first, second)]
        return calc(r, b, second, first)
    first = [1, 0]
    second = [0, 1]
    return calc(a, b, first, second)

def mod_inv(n, mod):
    table = gcd(n, mod)
    inv = table[1][1]
    if inv < 0:
        inv += mod
    return inv

def mod_pow(x, n, mod):
    ret = 1
    while n > 0:
        if n & 1 != 0:
            ret *= x
            ret %= mod
        x *= x
        x %= mod
        n >>= 1
    return ret

l = input().split()
Q = int(l[0])
X = []
D = []
N = []
for i in range(Q):
    l = input().split()
    X.append(int(l[0]))
    D.append(int(l[1]))
    N.append(int(l[2]))


for i in range(Q):
    x = X[i]
    d = D[i]
    n = N[i]
    if d == 0:
        print(mod_pow(x, n, mod))
        continue
    inv_d = mod_inv(d, mod)
    x_d = (x * inv_d) % mod
    # print(i, x, d, n, inv_d, x_d, x_d + n - 1)
    if x_d + n - 1 >= mod:
        print(0)
        continue
    ans1 = fac[x_d + n - 1]
    ans2 = fac[x_d - 1]
    # print(ans1, ans2)
    ans = ans1 * mod_inv(ans2, mod)
    ans %= mod
    d_n = mod_pow(d, n, mod)
    ans = ans * d_n
    ans %= mod
    print(ans)