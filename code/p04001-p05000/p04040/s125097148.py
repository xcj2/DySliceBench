P=10**9+7
def egcd(a, b):
    (x, lastx) = (0, 1)
    (y, lasty) = (1, 0)
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lastx) = (lastx - q * x, x)
        (y, lasty) = (lasty - q * y, y)
    return (lastx, lasty, a)
def inv(x):
    return egcd(x,P)[0]
H,W,A,B=map(int,input().split())
N=H+W
fact=[0 for i in range(N+1)]
finv=[0 for i in range(N+1)]
fact[0]=1
finv[0]=1
for i in range(1,N+1):
    fact[i]=(fact[i-1]*i)%P
    finv[i]=(inv(fact[i]))%P
def C(a,b):
    return (fact[a+b]*(finv[a]*finv[b])%P)%P
D=0
for i in range(B,W):
    K=(C(H-A-1,i)*C(A-1,W-1-i))%P
    D=(D+K)%P
print(D)
'''
HWAB
6734
4   C(2,4)*C(2,2)   15*6=90
5   C(2,5)*C(2,1)   21*3=63
6   C(2,6)*C(2,0)   28*1=28

'''