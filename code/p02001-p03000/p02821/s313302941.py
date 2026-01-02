n, m = map(int, input().split())
a = list(map(int, input().split()))

def cumsum(s):
    n = len(s)
    cs = [0] * (n+1)
    for i in range(n):
        cs[i+1] = cs[i] + s[i]
    return cs

def bs_list(a, f):
    l, r = -1, len(a)
    while r - l > 1:
        x = (l + r) // 2
        if f(a[x]): r = x
        else: l = x
    return None if r == len(a) else r

a.sort()
ca = cumsum(a)

def detect(x):
    num = 0
    for b in a[::-1]:
        res = bs_list(a, lambda y: y >= x - b)
        if res is None: break
        num += n - res
    return num <= m

l, r = -1, 10**5*2+10
while r - l > 1:
    x = (l+r) // 2
    if detect(x): r = x
    else: l = x

s, c = 0, 0
for b in a[::-1]:
    res = bs_list(a, lambda x: x >= r - b)
    if res is None: break
    c += (n - res)
    s += b * (n - res) + (ca[n] - ca[res])

print(s + (m - c) * l)
