MOD = 10**9 + 7

r1, c1, r2, c2 = map(int, input().split())

def getFact(n, MOD):
    fact = 1
    for i in range(1, n+1):
        fact = (fact * i) % MOD
    return fact
def getFacts(n, MOD):
    facts = [1] * (n+1)
    for x in range(2, n+1):
        facts[x] = (facts[x-1] * x) % MOD
    return facts
def getInvFacts(n, MOD):
    invFacts = [0] * (n+1)
    invFacts[n] = pow(getFact(n, MOD), MOD-2, MOD)
    for x in reversed(range(n)):
        invFacts[x] = (invFacts[x+1] * (x+1)) % MOD
    return invFacts

facts = getFacts(2*10**6+3, MOD)
invFacts = getInvFacts(10**6+3, MOD)

def f(r, c):
    ans = facts[r+c] * invFacts[r] * invFacts[c]
    return ans % MOD

#print(f(r2+1, c2+1), f(r2+1, c1), f(r1, c2+1), f(r1, c1))
ans = f(r2+1, c2+1) - f(r2+1, c1) - f(r1, c2+1) + f(r1, c1)
ans %= MOD

print(ans)
