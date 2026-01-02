a,b,c,d = map(int,input().split())

def f(x,y,p):
    res = 0
    if x%p == 0:
        start = x+1
        res += 1
    else:
        start = (x//p+1)*p
        if start > y:
            return 0
        if start == y:
            return 1
        start += 1
        res += 1
    return res+(y-start+1)//p

#a,bの最大公約数
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

#リスト l の最大公約数
def gcdlist(l):
    a = l[0]
    for i in range(len(l)):
        a = gcd(a,l[i])
    return a

#互いに素なa,bについて、a*x+b*y=1の一つの解
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

#a*x+b*y=gcd(a,b)の一つの解
def extgcd_2(a,b):    
    g = gcd(a,b)
    a = a//g
    b = b//g
    return extgcd(a,b)

#a,bの最小公倍数
def lcm(a, b):
	return a * b // gcd (a, b)

print(b-a+1-f(a,b,c)-f(a,b,d)+f(a,b,lcm(c,d)))