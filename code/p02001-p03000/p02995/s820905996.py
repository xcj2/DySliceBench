# x 以下でc, d 両方で割れない条件を満たす自然数の個数をf(x, c, d) とすると
# 求める値は f(b, c, d) - f(a-1, c, d)
# x 以下でk で割れる自然数の個数を g(x, k)とすれば
# f(x, c, d) = x - (g(x, c) + g(x, d) - g(x, lcm(c,d)))
# よって計算すべきは
# g(b, c) + g(b, d) - g(b, lcm(c,d)) - ( g(a-1, c) + g(a-1, d) - g(a-1, lcm(c,d)))
 
def gcd (p, q):
    temp = max(p, q)
    q = min(p, q)
    p = temp
    if q == 0:
        return p
    else:
        return gcd(q, p%q)
    
def lcm(p, q):
    return p * q // gcd(p, q)
 
def g(x, k):
    return x//k
 
def f(x, c, d):
    return x - (g(x, c) + g(x, d) - g(x, lcm(c,d)))
 
a,b,c,d = list(map(lambda x:int(x) ,input().split()))
 
print(f(b, c, d) - f(a-1, c, d))