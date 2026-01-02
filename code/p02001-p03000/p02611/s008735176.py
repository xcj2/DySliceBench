from functools import lru_cache

@lru_cache(102400)
def t(n, u):
    if u <= 0:
        return 1
    ans = 0
    for k1 in range(0, n + 1):
        for k2 in range(k1 + 1, (n - k1) + 1):
            ans += (k2 - k1) * t(n - k1 - k2, u - 1)
    return ans

def tl(n, u):
    return list(map(lambda x: t(x, u), range(n)))

def d(x):
    return [x[i + 1] - x[i] for i in range(len(x) - 1)]

l = tl(80, 5)
sp = [[], []]

for j in range(2):
    sp[j] = [(i, l[i]) for i in range(j, len(l), 2)]
    # u = [l[i] for i in range(j, len(l), 2)]
    # for k in range(30):
    #     print(u)
    #     u = d(u)

mo = 10 ** 9 + 7

def rev(x):
    global mo
    return pow(x, mo - 2, mo)

def solveKth(s, k):
    global mo
    for u, v in s:
        if u == k:
            return v % mo
    def l(j):
        global mo
        ans = 1
        for i in range(len(s)):
            if i != j:
                ans = ans * (k - s[i][0]) * rev(s[j][0] - s[i][0]) % mo
        return ans
    ans = 0
    for j in range(len(s)):
        ans = (ans + s[j][1] * l(j)) % mo
    return ans

t = int(input())
for _ in range(t):
    x = int(input())
    print(solveKth(sp[x % 2], x))