import math

def makelist(n, m):
    return [[0 for _ in range(m)] for _ in range(n)]

N, M = list(map(int, input().split()))
a = list(map(int, input().split()))

# 最小公倍数
# ユークリッドの互除法
def lcm(a, b): 
    def gcd(a, b):  # a >= b
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    
    return a * b // gcd(a, b)

c = 1
for e in a:
    c = lcm(c, e // 2)
hoge = [ (c // (e // 2)) % 2 == 1 for e in a ]

if all(hoge):
    ans = 0
    if c <= M:
        ans += 1
        M -= c
    ans += M // (c * 2)
    print(ans)
else:
    print(0)
