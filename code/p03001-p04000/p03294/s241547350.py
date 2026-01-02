#最大公約数
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#最大公約数の個数
def ngcd(a):
    res = a[0]
    for i in range(len(a)):
        if res != 1:
            res = gcd(a[i], res)
    return res

#最小公倍数
def lcm(a,b):
    return a * b // gcd(a, b)

#最小公倍数の個数
def nlcm(a):
    res = a[0]
    for i in range(len(a)):
        res = lcm(res, a[i])
    return res

n = int(input())
a = list(map(int, input().split()))

res = 1
for i in range(n):
    res = lcm(res, a[i])

res -= 1
ans = 0
for i in range(n):
    ans += res % a[i]
print(ans)
