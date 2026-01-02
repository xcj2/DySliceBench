from math import factorial
n, a, b = map(int, input().split())
if n == 2 and a == 1 and b == 2:
    print(0)
    exit()

mod = 10**9 + 7

limit = 0
m = n
while m > 0:
    m //= 2
    limit += 1
# print(limit)

def solve(n):
    ans = 1
    p = 2
    for i in range(limit):
        # print(i, (n >> i) & 1)
        if (n >> i) & 1 == 1:
            ans = (ans * p) % mod
        p = (p * p) % mod
    # print(p)
    return ans

ans = solve(n)
# print(ans)
# a1 = solve(a - 1)
# a2 = solve(a)
# a3 = (a1 - a2) % mod
# b1 = solve(b - 1)
# b2 = solve(b)
# b3 = (b1 - b2) % mod
# print((ans - a3 - b3) % mod)

def gcd1(a, b):
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
    table = gcd1(n, mod)
    inv = table[1][1]
    if inv < 0:
        inv += mod
    return inv

def cmb(n, r, mod):
    ans = 1
    for i in range(r):
        ans = (ans * n) % mod
        n -= 1
    ans1 = 1
    for i in range(1, r + 1):
        ans1 = (ans1 * i) % mod
    return ans * mod_inv(ans1, mod)

# f_n = factorial(n) % mod
# f_a = factorial(a) % mod
# f_b = factorial(b) % mod
# f_na = factorial(n - a) % mod
# f_nb = factorial(n - b) % mod
# print(f_n, f_a, f_b, f_na, f_nb)
# ac = (f_n * mod_inv(f_a, mod)) % mod
# ac = (ac * mod_inv(f_n_a, mod)) % mod
# bc = (f_n * mod_inv(f_b, mod)) % mod
# bc = (bc * mod_inv(f_n_b, mod)) % mod

ac = cmb(n, a, mod)
bc = cmb(n, b, mod)

# print(ans, ac, bc)
print((mod + ans - ac - bc - 1) % mod)
