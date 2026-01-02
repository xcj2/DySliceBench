def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))

n, k = getList()
MOD = 1000000007

def make_factorial(n, mod):
    fact = [1]
    tmp = 1
    for i in range(1, n+1):
        tmp *= i
        # tmp = tmp % mod
        fact.append(tmp)

    return fact


factorial = make_factorial(n, MOD)
def nck(fact, n, k):
    return fact[n] // (fact[k] * fact[n-k])


def solve(r, b, k, fact):
    if b > r + 1:
        print(0)
        return

    sukima = nck(fact, r+1, b)
    amari = k - b
    tyohuku = nck(fact, k-1, b-1)
    tyohuku = tyohuku % MOD

    # print(sukima, amari, tyohuku)
    print((sukima * tyohuku) % MOD)
    return


for trial in range(1, k+1):
    solve(n - k , trial, k, factorial)