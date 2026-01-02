X, Y = map(int, input().split())

import sys
if (-X+2*Y)%3 != 0 or (2*X-Y)%3 != 0:#桂馬跳びでは到達できない
    print(0)
    sys.exit()
x, y = (-X+2*Y) // 3, (2*X-Y) // 3
if x < 0 or y < 0:#盤面外
    print(0)
    sys.exit()
    
P = 1000000007

def mul(a, b):
    return ((a % P) * (b % P)) % P
 
def div(x, y):
    return mul(x, pow(y, P-2, P))
 
def comb(n, r):
    x = 1
    for i in range(n, n - r, -1):
        x = (x * i) % P
        
    y = 1
    for i in range(1, r+1):
        y = (y * i) % P
    return div(x, y)

print(comb(x + y, min(x, y)))