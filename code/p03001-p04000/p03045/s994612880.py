#最大公約数
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

#最小公倍数
def lcm(x, y):
    return (x * y) // gcd(x, y)

#エストラテネスの篩
def isPrime():
    MAX = 10**5
    is_prime = [1] * (MAX+1)
    is_prime[0] = 0
    is_prime[1] = 0
    for i in range(2, MAX+1):
        if is_prime[i]:
            for j in range(i*2, MAX+1, i):
                is_prime[j] = 0
    return is_prime

#約数を求める
def makeDivisor(n):
    divisors = []
    for i in range(1, int(n ** 0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

#素因数分解（試し割り法）
def makePrime(n):
    factor = []
    tmp = int(n ** 0.5) + 1
    for num in range(2, tmp):
        while n % num == 0:
            n //= num
            factor.append(num)

    if n > 1:
        factor.append(n)

    return factor

#繰り返し２乗法
def modPow(a, p):
    if p == 0:
        return 1
    if p % 2 == 0:
        halfP = p // 2
        half = modPow(a, halfP)
        return half * half % mod
    else:
        return a * modPow(a, p-1) % mod

#組み合わせ
def comb(a, b):
    if b > a - b:
        return comb(a, a-b)
    ansMul = 1
    ansDiv = 1
    for i in range(b):
        ansMul *= a - i
        ansDiv *= i + 1
        ansMul %= mod
        ansDiv %= mod

    ans = ansMul * modPow(ansDiv, mod-2) % mod
    return ans

#UnionFind
class UnionFind():

    def __init__(self, n):
        self.n = n
        self.root = [-1] * (n+1)

    def FindRoot(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.FindRoot(self.root[x])
            return self.root[x]

    def Unite(self, x, y):
        x = self.FindRoot(x)
        y = self.FindRoot(y)

        if x == y:
            return False
        if self.Size(x) < self.Size(y):
            x, y = y, x
        self.root[x] += self.root[y]
        self.root[y] = x

        return True

    def isSameGroup(self, x, y):
        return self.FindRoot(x) == self.FindRoot(y)

    def Size(self, x):
        return -self.root[self.FindRoot(x)]

N, M = map(int, input().split())
X = [0] * M
Y = [0] * M
Z = [0] * M
for i in range(M):
    X[i], Y[i], Z[i] = map(int, input().split())

Uni = UnionFind(N)

for i in range(M):
    Uni.Unite(X[i], Y[i])

roots = set()
for i in range(1, N+1):
    roots.add(Uni.FindRoot(i))

print(len(roots))
