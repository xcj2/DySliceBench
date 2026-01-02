n, m = [int(i) for i in input().split()]
prime = 10 ** 9 + 7

def fact(x):
    a = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            j = 0
            while x % i == 0:
                x //= i
                j += 1
            a.append((i, j))
    if x != 1:
        a.append((x,1))
    return a


f = fact(m)
def kai(x):
    a = 1
    for i in range(a, x + 1):
        a *= i
        a %= prime
    return a

def conv(a, b):
    c = kai(b)
    c *= pow(kai(a), prime - 2, prime)
    c %= prime
    c *= pow(kai(b - a), prime - 2, prime)
    return c % prime


ans = 1
for i in f:
    ans *= conv(n - 1, n + i[1] - 1)
    ans %= prime
print(ans)
