def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def div2(x):
    c = 0
    while x%2==0:
        x //= 2
        c+=1
    return c

def test():
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(N):
        if a[i]%2 == 1:
            return 0
        a[i] //= 2

    t = div2(a[0])
    for i in range(N):
        if div2(a[i]) != t:
            return 0
        a[i] >>= t
    M >>= t

    L = a[0]
    for i in range(1, N):
        L = lcm(L, a[i])
        if L > M:
            return 0

    ans = (M-L)//(2*L)+1
    return ans

print(test())