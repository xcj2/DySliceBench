x,y = map(int,input().split())
M = 10**9+7

def pow(a,b,M):
    if b == 0:
        return 1
    else:
        if b % 2 == 0:
            return pow((a**2)%M,b//2,M) % M
        else:
            return (a * pow((a**2)%M,b//2,M)) % M

def inv(a,M):
    return pow(a,M-2,M)

def comb(n,k,M):
    nume,deno = 1,1
    for i in range(1,k+1):
        deno = (deno * (n-i+1)) % M
        nume = (nume * i) % M
    return (deno * inv(nume,M)) % M

if (x+y) % 3 != 0 or (2*x < y or 2*y < x):
    print(0)
else:
    mov = (x+y)//3
    x,y = x-mov,y-mov
    print(comb(mov,x,M))
