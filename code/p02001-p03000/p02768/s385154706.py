def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def invmod(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
    
def left_bin(a, n, c):
    ns = [int(i) for i in bin(n)[3:]]
    t = a
    for i in ns:
        t = t*t % c
        if i == 1:
            t = t*a % c
    return t

n, a, b = map(int, input().split())
c = 10**9 + 7

ans = left_bin(2, n, c) - 1 
temp = n
if a == 1:
    ans = (ans - n) % c
for i in range(1, b):
    temp = temp*(n-i) % c
    temp = temp*invmod(i+1, c) % c
    if i+1 == a:
        ans = (ans - temp) % c
ans = (ans - temp) % c
print(ans)
