from sys import stdin
import numpy as np
mod = 10**9+7
X,Y = [int(x) for x in stdin.readline().rstrip().split()]

def mul(a, b):
    return ((a % mod) * (b % mod)) % mod
 
def power(x, n):
    """
    O(log n)
    """
    if n == 0:
        return 1
 
    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x % mod
        x *= x % mod
        n //= 2
 
    return K * x % mod
 
def div(a, b):
    return mul(a, power(b, mod-2))
 
def fact(n):
    f = 1
    for i in range(1,n+1):
        f *= i
        f %= mod
    return f

if (X+Y) % 3 != 0:
    print(0)

else:
    A = np.matrix([[2, 1],[1, 2]])
    Y = np.matrix([[X],[Y]])
    x,y = np.linalg.solve(A,Y)
    x = int(x)
    y = int(y)
    ans = fact(x+y)
    ans = div(ans,fact(x))
    ans = div(ans,fact(y))
    if x < 0 or y <0:
        print(0)
    else:
        print(ans%mod)