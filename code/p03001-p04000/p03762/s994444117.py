import sys
stdin = sys.stdin

def li(): return [int(x) for x in stdin.readline().split()]
def li_(): return [int(x)-1 for x in stdin.readline().split()]
def lf(): return [float(x) for x in stdin.readline().split()]
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(ns())
def nf(): return float(ns())

MOD = 10**9+7

n,m = li()
x = li()
y = li()

x.sort(reverse=True)
y.sort(reverse=True)

x_coeff = [n-(2*i+1) for i in range(n)]
y_coeff = [m-(2*i+1) for i in range(m)]

x_sum = 0
y_sum = 0

for xi, xcoefi in zip(x, x_coeff):
    x_sum += (xi * xcoefi)
    x_sum %= MOD
    
for yi, ycoefi in zip(y, y_coeff):
    y_sum += (yi * ycoefi)
    y_sum %= MOD

ans = x_sum * y_sum
print(ans%MOD)