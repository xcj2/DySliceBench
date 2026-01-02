def divisor(n):
    ret = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ret.append(i)
            if i*i != n:
                ret.append(n//i)
    return ret
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def extgcd(a, b):
    x0, x1, y0, y1 = 0,1,1,0
    while a:
        g,b,a = b//a, a, b%a
        y0,y1 = y1, y0-g*y1
        x0,x1 = x1, x0-g*x1
    return x0, y0, b

def get_t(A,y):
    ta = int(-A/y) + 1
    if -A < 0 and A%y != 0:
        ta = int(-A/y)
    return ta

n = int(input())
if n == 2:
    k = 3
elif is_prime(n):
    k = n-1
else:
    k = float("inf")
    n = 2*n
    div = divisor(n)
    for x in div:
        y = n//x
        A, B, g = extgcd(x, -y)
        if g == 1:
            ta = get_t(A, y)
            tb = get_t(B, y)
            t = max(ta, tb)
            a = A + y*t
            b = B + x*t
            ax = a*x
            by = b*y
            k = min(k, by)

print(k)

