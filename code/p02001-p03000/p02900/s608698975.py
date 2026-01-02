def gcd_core(a, b):
    if b == 0:
        return a
    else:
        return gcd_core(b, a % b)
def gcd(arr):
    g = gcd_core(arr[0], arr[1])
    for i in range(2, len(arr)):
        g = gcd_core(g, arr[i])
    return g
def lcm_core(a,b):
    g = gcd_core(a,b)
    return (a*b)//g
def lcm(arr):
    l = lcm_core(arr[0],arr[1])
    for i in range(2,len(arr)):
        l = lcm_core(l,arr[i])
    return l
def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table
def isprime(p):
    x = 2
    while x*x <= p:
        if p%x == 0:
            return False
        x += 1
    return True

A, B = map(int, input().split())
ans = 0
for i in set(divisor(A)) & set(divisor(B)):
    if isprime(i):
        ans += 1
print(ans)