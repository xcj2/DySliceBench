import sys

fact = [1]
p = 10**9 + 7

def fact1(n,m):
    for i in range(1,n+m+1):
        new_fact = fact[i-1]*i %p
        fact.append(new_fact)

#ax+by=1の解
def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2] != 1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2

    return [w[0],w[1]]
#aの逆元(mod m) a,mは互いに素
def mod_inv(a,m):
    x = extgcd(a,m)[0]
    return x%m
if __name__ == "__main__":
    x, y = (int(i) for i in input().split())
    if (x+y)%3 != 0 or 2*x < y or 2*y < x:
        print(0)
        exit()
    n = int((2*y-x)/3)
    m = int((2*x-y)/3)
    fact1(n,m)
    n1 = mod_inv(fact[n],p)
    m1 = mod_inv(fact[m],p)
    ans = fact[n+m] * (n1*m1 %p) % p
    print(ans)
