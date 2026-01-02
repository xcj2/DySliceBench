def gcd(a,b):
	if a > b:
		n,m = a,b
	else:
		n,m = b,a
	while m > 0:
		t = n % m
		n = m
		m = t
	return n

def gcd_3(a,b,c):
	return gcd(gcd(a,b),c)

g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

N,A,B,K = map(int,input().split())
g = gcd_3(A,B,K)
A = A // g
B = B // g
K = K // g
mod = 998244353 #出力の制限
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

ans = 0
n0,m0=-1,-1
for i in range(K//A + 1):
	if (K - A*i) % B == 0:
		n0,m0 = i, (K - A*i)//B
		break
k = 0
while k*B + n0 <= N and m0 - k*A >= 0:
	n,m = k*B + n0, m0 - k*A
	if m <= N:
		ans = (ans + cmb(N,n,mod) * cmb(N,m,mod)) % mod
	k += 1
print(ans)