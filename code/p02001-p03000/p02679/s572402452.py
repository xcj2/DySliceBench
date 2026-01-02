import sys
input = sys.stdin.readline

n = int(input())
A = [list(map(int,input().split())) for i in range(n)]
mod = 10**9 + 7
l = 2*10**5 + 10

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


M2 = [1]
for i in range(l):
    M2.append((M2[-1] * 2) % mod)

import math

D = {}
m = 0
for i in range(n):
    x = A[i][0]
    y = A[i][1]
    if x != 0 or y != 0:
        m += 1
        
        s = 0
        while not (x >= 0 and y > 0):
            x, y = -y, x
            s += 1
        g = math.gcd(x, y)
        x //= g
        y //= g
        try:
            D[(x,y)][s] += 1
        except:
            D[(x,y)] = [0,0,0,0]
            D[(x,y)][s] += 1
    
# print(D,m)

def minus(ll,x):
    ans0 = 0
    # hu = -1
    for i in range(2, x+1):
        ans0 = (ans0 + M2[ll-x] * C(x, i)) % mod
        # hu *= -1
    return ans0

# ans = M2[m] - 1 + (n-m)
ans = 1
DV = list(D.values())
ld = len(DV)
# print(DV)
for i in range(len(DV)):
    s = sum(DV[i])
    s0 = DV[i][0] + DV[i][2]
    s1 = DV[i][1] + DV[i][3]
    ans = (ans * (M2[s0] + M2[s1] - 1)) % mod
    # print(s,s0,s1)
    # print(minus(s) ,minus(s0) , minus(s1))
    # ans = (ans - minus(ld,s) + minus(s0,s-s0) + minus(s1,s-s1)) % mod

print((ans-1 + (n-m)) % mod)
