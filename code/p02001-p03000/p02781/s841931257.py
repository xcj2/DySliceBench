n = input()
kk = int(input())

mod = 10**9 + 7
l = 2*10**2

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
k = kk
for i in range(len(n)):
    s = int(n[i])
    z = len(n)-i-1
    # print(s,z)
    if s >= 1 and k >= 0:
        ans += C(z, k) * (9**k) + C(z, k-1) * (9**(k-1)) * (s-1)
        k -= 1
    # print("ans",ans)
if n.count("0") == len(n)-kk:
    ans += 1
print(int(ans))