#a,bの最大公約数
def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

#a,bの最小公倍数
def lcm(a,b):
    return a*b//gcd(a,b)

#べき乗関数powを使った逆元の計算(modinvよりもPythonでは高速、PyPyだと遅い)
def modinv2(a,m):
    return pow(a,m-2,m)


N = int(input())
A = list(map(int,input().split()))
P = 10**9+7

if N == 1:
    ans = 1

else:

    inv = modinv2(A[0],P)
    g = A[0]
    invlist = []
    seki = A[0]%P

    for i in range(1,N):
        inv = (inv+modinv2(A[i],P))%P
        seki = seki*A[i]%P

    g = gcd(A[0],A[1])
    l = A[0]//g*A[1]
    cc = modinv2(g,P)
    for i in range(2,N):
        g = gcd(l,A[i])
        l = l//g*A[i]
        cc = cc*modinv2(g,P)%P

    ans = (inv*seki%P)*cc%P

print(ans)