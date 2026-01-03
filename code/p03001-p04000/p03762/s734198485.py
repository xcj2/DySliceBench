n, m = list(map(int, input().split()))

xs = list(map(int, input().split()))
ys = list(map(int, input().split()))

MODULO = 10**9 +7

def MSum(x, y):
    return (x + y) % MODULO

def MPro(x, y):
    return (x * y) % MODULO

def foo(zs, k):
    s = 0
    for i in range(k):
       s = MSum(s, MPro(MPro(zs[i], k-i), i+1))
    return s

def diff(zs, k):
    previous = None
    rs = [0] * (k-1)
    for i, z in enumerate(zs):
        if i == 0:
            previous = z
            continue
        rs[i-1] = z - previous
        previous = z
    return rs

dx = diff(xs, n)
dy = diff(ys, m)

print(MPro(foo(dx, n-1), foo(dy, m-1)))

