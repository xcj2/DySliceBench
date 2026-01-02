import math

mod = 10**9 + 7
n2 = 2**100 % (mod)
n4 = n2**100 % (mod)
n6 = n4**100 % (mod)
n8 = n6**100 % (mod)


def iip():
    return [int(i) for i in input().split()]

def power(n, p):
    if p == 0:
        return 1
    if p % 2 == 0:
        return (power(n, p/2) ** 2) % mod
    if p % 2 == 1:
        return (n * power(n, p-1)) % mod

def conbination(n, r):
    #print("conbination")
    ret = 1
    for i in range(1, r+1):
        ret *= (i+n-r)
        ret = ret % mod

    ret *= power(math.factorial(r), mod-2)
    ret = ret % mod

    #print(f"conbination {n}, {r} = {ret}")
    return ret

def binaly(n):
    return power(2, n)


def raw(n, a, b):
    d = binaly(n)
    c1 = conbination(n, a)
    c2 = conbination(n, b)
    return d - c1 - c2 - 1

def answer(n, a, b):
    return raw(n, a, b) % (10**9+7)

n, a, b = iip()

#print(factorial(1000000))
#print(math.factorial(1000000)%mod)
print(answer(n, a, b))
