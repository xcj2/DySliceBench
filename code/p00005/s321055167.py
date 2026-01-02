def pd(n):
    i = 2
    ans = []
    while i ** 2 <= n:
        while n % i == 0:
            n /= i
            ans.append(i)
        i += 1
    if n > 1:
        ans.append(n)
    return ans

def gcd(a, b):
    gcd = 1
    pd_a = pd(a)
    pd_b = pd(b)
    for i in pd_a:
        if i in pd_b:
            pd_b.remove(i)
            gcd *= i
    return int(gcd)

def lcm(a, b):
    lcm = a
    pd_a = pd(a)
    pd_b = pd(b)
    for i in pd_a:
        if i in pd_b:
            pd_b.remove(i)
    for j in pd_b:
        lcm *= j
    return int(lcm)

while True:
    try:
        s = input()
        a,b = [int(i) for i in s.split(' ')]
    except:
        break
    print(gcd(a, b), lcm(a, b))
