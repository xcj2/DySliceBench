MOD = 10 ** 9 + 7

n, k = map(int, input().split())
a = sorted(map(int, input().split()))

factorialNumInverse = [None] * (n + 1)
naturalNumInverse = [None] * (n + 1)
fact = [None] * (n + 1)

def inverseofNumber():
    naturalNumInverse[0] = naturalNumInverse[1] = 1
    for i in range(2, n + 1):
        naturalNumInverse[i] = (naturalNumInverse[MOD % i] * (MOD - MOD // i) % MOD)

def inverseofFactorial():
    factorialNumInverse[0] = factorialNumInverse[1] = 1
    for i in range(2, n + 1):
        factorialNumInverse[i] = (naturalNumInverse[i] * factorialNumInverse[i - 1]) % MOD

def factorial():
    fact[0] = 1
    for i in range(1, n + 1):
        fact[i] = (fact[i - 1] * i) % MOD

inverseofNumber()
inverseofFactorial()
factorial()

def nCk(n, k):
    ans = ((fact[n] * factorialNumInverse[k]) % MOD * factorialNumInverse[n - k]) % MOD
    return ans

def calcSum(a):
    ret = 0
    for i in range(k - 1, n):
        ret += (nCk(i, k - 1) * a[i]) % MOD
        ret %= MOD
    return ret

print((calcSum(a) - calcSum(a[::-1])) % MOD)