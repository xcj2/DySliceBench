
def extgcd(a, b):
    r = [1, 0, a]
    w = [0, 1, b]
    while w[2] != 1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0], r[1]-q*w[1], r[2]-q*w[2]]
        r = r2
        w = w2
    #[x,y]
    return [w[0], w[1]]


def mod_inv(a, m):
    x = extgcd(a, m)[0]
    return (m+x % m) % m


def mod_e(n, p):
    res = 0
    while n >= p:
        res += n//p
        n = n//p
    return res


def mod_fact(n, p):
    if n == 0:
        return 1

    res = mod_fact(n//p, p)

    if n//p % 2 != 0:
        return res*(p-fact[n % p]) % p
    return res*fact[n % p] % p


# nCk mod p
def mod_comb(n, k, p):
    if n < 0 or k < 0 or n < k:
        return 0
    e1 = mod_e(n, p)
    e2 = mod_e(k, p)
    e3 = mod_e(n-k, p)
    #pで割り切れる場合
    if e1 > e2 + e3:
        return 0

    #pで割り切れない場合
    a1 = mod_fact(n, p)
    a2 = mod_fact(k, p)
    a3 = mod_fact(n-k, p)
    return a1 * mod_inv(a2*a3 % p, p) % p

X, Y = map(int, input().split())
x = (2 * Y - X) / 3
y = (2 * X - Y) / 3

# print(x, y)

if (2 * Y - X) % 3 != 0 or (2 * X - Y) % 3 != 0:
    print(0)
    exit()
else:
    x = int(x)
    y = int(y)

if x < 0 or y < 0:
    print(0)
    exit()
# print(x,y)
if x < y:
    x, y = y, x

#pは素数とする
p = 10**9+7

#fact[i] : i! modp (0<= i <p) O(p)
#上だとO(p)なのでnまでにして O(n)にする
fact = [1]
k = 1
for i in range(1, 10**6+100):
    k = k*i % p
    fact.append(k)

#10000C4000 mod 10**9+7
print(mod_comb(x + y, y, p))
