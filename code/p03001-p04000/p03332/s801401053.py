n, a, b, k = map(int,input().split())

mod = 998244353
l = 3*10**5 + 3

M = [1]  # i!のmod
m = 1
for i in range(1, l):
    m = (m * i) % mod
    M.append(m)

def pow(x, y, mod):  # x**y の mod を返す関数
    ans = 1
    while y > 0:
        if y % 2 == 1:
            ans = (ans * x) % mod
        x = (x**2) % mod
        y //= 2
    return ans

def inv(x, mod):  # x の mod での逆元を返す関数
    return pow(x, mod-2, mod)

# print(inv(8,13))

MI = [0] * (l-1) +[inv(M[l-1], mod)]  # i!の逆元
for i in range(l-2, -1, -1):
    MI[i] = MI[i+1] * (i+1) % mod

def C(x, y):  # コンビネーション
    if y < 0 or y > x:
        return 0
    ans = M[x]
    ans = (ans * MI[y]) % mod
    return (ans * MI[x-y]) % mod

ans = 0
for i in range(n+1):
    c0n = i
    c1 = k-i*a
    if c1 % b == 0 and 0 <= c1 // b <= n:
        c1n = c1 // b
        # print(c0n,c1n)
        ans = (ans + C(n, c0n) * C(n, c1n)) % mod
print(ans%mod)