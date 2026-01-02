import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())


def floor_sum(n,m,a,b):  # sum((A*i+B)//M for i in range(N))
    res = 0
    if a >= m:
        res += (a//m)*n*(n-1)//2
        a %= m
    if b >= m:
        res += (b//m)*n
        b %= m
    y_max = (a*n+b)//m
    if y_max == 0:
        return res
    x_max = m*y_max-b
    res += (n+(-x_max)//a)*y_max
    res += floor_sum(y_max,a,m,(-x_max) % a)
    return res


T = I()
for i in range(T):
    n,m,a,b = MI()
    print(floor_sum(n,m,a,b))
