N = int(input())
X = list(map(int,input().split()))
mod = 10**9 + 7

def euclid(a:int,b:int)->(int,int):
    #return x,y s.t ax + by = gcd(a,b)
    #a > b >= 0
    if b == 0:
        return 1,0
    x,y = euclid(b,a%b)
    return y,x - y*(a // b)

def inverse(a:int,mod:int)->int:
    #gcd(p,b) == 1
    if mod > a:
        n,x = euclid(mod,a)
    else:
        x,n = euclid(a,mod)
    return x

def devide_mod(a:int,b:int,mod:int)->int:
    #a // b
    x = inverse(b,mod)
    return  (a*x)%mod


def main():
    ans = 0
    fraq = [1]*(N)
    S = [0]*(N+1)
    for i in range(1,N):
        fraq[i] = (fraq[ i - 1 ]*i)%mod
    
    for i in range(1,N + 1):
        S[ i ] = (S[ i - 1 ] + devide_mod(fraq[ N - 1 ], i ,mod))%mod

    for i in range(N - 1):
        ans = (ans + (X[ i + 1 ] - X[ i ])*S[ i + 1 ])%mod
    print(ans)
    return

if __name__ == "__main__":
    main()