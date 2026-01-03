import collections

# Iterative Algorithm (xgcd)
def iterative_egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q,r = b//a,b%a; m,n = x-u*q,y-v*q # use x//y for floor "floor division"
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y
 
# Recursive Algorithm
def recursive_egcd(a, b):
    """Returns a triple (g, x, y), such that ax + by = g = gcd(a,b).
       Assumes a, b >= 0, and that at least one of them is > 0.
       Bounds on output values: |x|, |y| <= max(a, b)."""
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = recursive_egcd(b % a, a)
        return (g, x - (b // a) * y, y)
 
egcd = iterative_egcd  # or recursive_egcd(a, m)
 
def modinv(a, m):
    g, x, y = egcd(a, m) 
    if g != 1:
        return None
    else:
        return x % m
 
def conv(n,a):
    ret = 1
    for i in range(1,a+1):
        ret *= n-a+i
        ret //= i
    return ret
        
n,a,b = map(int, input().split(' '))
v = map(int, input().split(' '))

v = sorted(v, reverse=True)
select = v[:a]
result1 = sum(select)/len(select)

result2 = 0
v_cnt = collections.Counter(v)
for i in range(a,b+1):
    select = v[:i]
    if result1 == sum(select)/len(select):
        select = collections.Counter(select)
        buf = 1
        for v_ in v_cnt:
            buf *= conv(v_cnt[v_],select[v_])
        result2 += buf
print('%.6f'%result1)
print(result2)