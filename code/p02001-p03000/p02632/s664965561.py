# import sys
# input = sys.stdin.readline
k = int(input())
s = input()
n = len(s)
mod = 10**9 + 7
l = 2*10**6 + 3

a25 = [1]
for i in range(l):
    a25.append((a25[-1] * 25) % mod)
a26 = [1]
for i in range(l):
    a26.append((a26[-1] * 26) % mod)


mod = 10**9 + 7


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
    elif x > l:  # O(min(y, x-y))
        y = min(y, x-y)
        ans = 1
        for i in range(x, x-y, -1):
            ans = (ans * i) % mod
        return (ans * MI[y]) % mod
    else:  # O(1)
        ans = M[x]
        ans = (ans * MI[y]) % mod
        return (ans * MI[x-y]) % mod

ans = 0
for i in range(n-1, n+k):
    ans = (ans + C(i, n-1) * a25[i-(n-1)] * a26[n+k-i-1]) % mod
print(ans)