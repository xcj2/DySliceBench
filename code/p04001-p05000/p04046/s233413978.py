def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def egcd(a, b):
    (x, lastx) = (0, 1)
    (y, lasty) = (1, 0)
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lastx) = (lastx - q * x, x)
        (y, lasty) = (lasty - q * y, y)
    return (lastx, lasty, a)

# ax ≡ 1 (mod m)
def modinv(a, m):
    (inv, q, gcd_val) = egcd(a, m)
    return inv % m
N = 10**9+7
R = 10**5*2
modfact = [0]*(R+1)
def modfact_memo(n,N):
    r = 1
    modfact[0] = 1
    for i in range(1,n+1):
        r = r % N * i % N
        modfact[i] = r
modfact_memo(R,N)

# ax ≡ 1 (mod m)
modinv=[0]*(R+1)
def modinv_memo(a,m):
    for i in range(a+1):
        j = modfact[i]
        (inv, q, gcd_val) = egcd(j, m)
        modinv[i] = inv % m
modinv_memo(R,N)

def modconb(n,r,N):
    p = modfact[n]
    q1 = modinv[r]
    q2 = modinv[n-r]
    return p*q1%N*q2%N

H,W,A,B = map(int,input().split())
ans = 0
for r in range(B,W):
    ans += modconb(H-A-1+r,r,N)*modconb(A-1+W-r-1,A-1,N)
    ans %= N

print(ans)