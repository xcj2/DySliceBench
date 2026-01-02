def gcd(a, b):
    if a < b: a, b = b, a
    while b > 0:
        r = a % b
        a, b = b, r
    return a

def lcm(a,b):
    return ((a*b) // gcd(a,b))

def getCnt(a,m):
    cnt = 0
    n = 1
    while(1):
        n = (a * n) % m
        cnt += 1
        if n == 1:
            return cnt

while(1):
    a1,m1,a2,m2,a3,m3 = (int(x) for x in input().split())
    if a1 == 0:
        break
    x = y = z = 1
    cnt1 = getCnt(a1,m1)
    cnt2 = getCnt(a2,m2)
    cnt3 = getCnt(a3,m3)

    ans = lcm(cnt1,cnt2)
    ans = lcm(ans,cnt3)
    print(ans)
