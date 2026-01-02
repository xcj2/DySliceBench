def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2]!=1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    #[x,y]
    return [w[0],w[1]]


def mod_inv(a,m):
    x = extgcd(a,m)[0]
    return (m+x%m)%m


def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a


def lcm(a,b):
    return a*b//gcd(a,b)


p = 10**9+7
N = int(input())
mul = 1
inv_sum = 0
for x in input().split():
    a = int(x)
    inv_sum += mod_inv(a, p)
    inv_sum %= p
    mul = lcm(mul, a)

print(mul * inv_sum % p)