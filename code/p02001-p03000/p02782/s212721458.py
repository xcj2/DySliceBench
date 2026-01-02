r1,c1,r2,c2 = map(int,input().split())

mod = 10**9 + 7
l = 2*10**6 + 3

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
for i in range(r1, r2+1):
    ans = (ans + C(i+1+c2, c2) - C(i+c1, c1-1)) % mod
print(ans)