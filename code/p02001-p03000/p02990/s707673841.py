import math
sosu = 10 ** 9 + 7
N, K = map(int, input().split())
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

# aの逆元(mod m)を求める。(aとmは互いに素であることが前提)
def mod_inv(a,m):
    x = extgcd(a,m)[0]
    return (m+x%m)%m

def conv(n, r):
    bunbo = math.factorial(n) % sosu
    bunsi1 = mod_inv(math.factorial(r), sosu)
    bunsi2 = mod_inv(math.factorial(n-r), sosu)
    ans = bunbo * bunsi1 * bunsi2 % sosu
    return(ans)
#print(conv(1997,2))

for i in range(1, K+1):
    if N-K+1 >= i:
        fir = conv(K-1, i-1)
        sec = conv(N-K+1, i)
        ans = fir * sec % sosu
        print(int(ans))
    else:
        print(0)
