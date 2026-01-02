import math
from fractions import Fraction
import sys


class multipliable_2x2matrix(object):
    def __init__(self, a, b, c, d):
        self.a = a;
        self.b = b;
        self.c = c;
        self.d = d;
    def mul(self, b):
        return multipliable_2x2matrix(
            self.a * b.a + self.b * b.c,
            self.a * b.b + self.b * b.d,
            self.c * b.a + self.d * b.c,
            self.c * b.b + self.d * b.d)
    
def fib(n):
    if n == 0: return 0
    m = multipliable_2x2matrix(1, 1, 1, 0)
    f = multipliable_2x2matrix(1, 0, 0, 1)
    n = n - 1
    while n > 0:
        if n & 1 == 1:
            f = f.mul(m)
        n = n >> 1
        m = m.mul(m)
    return f.a



n, m =map(int, input().split())  #複数数値入力
a = [-1]
for i in range(m):
    ai = int(input())
    a.append(ai)
a.append(n+1)

count = 1
root5 = math.sqrt(5)
for i in range(m+1):
    x = a[i+1] - a[i] -1
    if x == 0:
        count = 0
        break
    else:
#         y = 1/root5 *(((1+root5)/2)**x - ((1-root5)/2)**x) 
        count *= fib(x)
print(int(count)%1000000007)