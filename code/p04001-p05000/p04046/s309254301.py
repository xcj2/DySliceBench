def ext_gcd(a,b):
    """returns tuple (gcd(a,b), x, y) s.t. ax+by=gcd(a,b)"""
    if b==0:
        return (a,1,0)
    g,x,y = ext_gcd(b,a%b) 
    return (g,y,x-a//b*y)
def invmod_by_gcd(a,P):
    _,x,y = ext_gcd(a,P)
    return (x+P) % P

F = []
FInv = []

def init_factorials(L,P):
    """initialize F and FInv less than L"""
    global F, FInv
    F = [1 for _ in range(L)]
    for i in range(1,L):
        F[i] = (F[i-1]*i)%P
    FInv = [1 for _ in range(L)]
    FInv[L-1] = invmod_by_gcd(F[L-1],P)
    for i in range(L-2,0,-1):
        FInv[i] = (FInv[i+1]*(i+1))%P
      
def combination(a, b, P):
    return (F[a]*FInv[b]*FInv[a-b])%P

P = 10**9+7 
H,W,A,B = map(int,input().split())

init_factorials(H+W,P)

ans = 0
for k in range(H-A):
    a = combination(B+k-1,B-1,P)
    b = combination(H+W-k-B-2,H-1-k,P)
    ans = (ans + a*b%P)%P
print(ans)
