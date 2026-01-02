
def poly_divide(f, g):
    n = len(g)
    a, b = f
    q = [0]*(n-1)
    r = 0
    q[-1] = g[-1]*inv[b%p]%p
    for i in range(n-2)[::-1]:
        q[i] = (g[i+1]-q[i+1]*a)*inv[b%p]%p
    r = g[0]-q[0]
    return q, r
  
def poly_product(f, g):
    n, m = len(f), len(g)
    res = [0]*(n+m-1)
    for i in range(n):
        for j in range(m):
            res[i+j]+=g[j]*f[i]
            res[i+j]%=p
    return res
def assign(f, x):
    tmp = 1
    res = 0
    n = len(f)
    for i in range(n):
        res+=f[i]*tmp
        tmp*=x
        tmp%=p
        res%=p
    return res
def c_mul(c, f):
    n = len(f)
    for i in range(n):
        f[i]*=c
        f[i]%=p
    return f
def poly_add(f, g):
    n = len(g)
    for i in range(n):
        f[i]+=g[i]
        f[i]%=p
    return f


p = int(input())
a = list(map(int, input().split()))
inv = [0]*p
P = [1]
for i in range(p):
    inv[i] = pow(i, p-2, p)
for i in range(p):
    b = [-i, 1]
    P = poly_product(b, P)
R = [0]*p
for i in range(p):
    b = [-i, 1]
    Q, _ = poly_divide(b, P)
    v = assign(Q, i)
    Q=c_mul(inv[v%p]*a[i], Q)
    R = poly_add(R, Q)
print(*R)
    
    





