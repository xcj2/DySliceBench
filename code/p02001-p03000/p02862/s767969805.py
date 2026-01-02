import sys
from math import factorial
sys.setrecursionlimit(100000)

input = sys.stdin.readline

X, Y = list(map(int,input().split()))

mod = 10**9 + 7

def mm(a, b):
    return ((a % mod) * (b % mod)) % mod

def pp(x, y):
    if   y == 0     :
    	return 1
    elif y == 1     : 
    	return x % mod
    elif y % 2 == 0 : 
    	return (pp(x, y/2)**2) % mod
    else            : 
    	return (pp(x, y//2)**2 * x) % mod

def dd(a, b):
    return mm(a, pp(b, mod-2))

def xgcd(a, b):
	x0, y0, x1, y1 = 1, 0, 0, 1
	while b != 0:
	    q, a, b = a // b, b, a % b
	    x0, x1 = x1, x0 - q * x1
	    y0, y1 = y1, y0 - q * y1
	return a, x0, y0

def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

if (X+Y)%3!=0:
	ans = 0
else:
	nmsum = (X+Y)//3
	nmdif = Y-X
	if (nmsum+nmdif)%2!=0:
		ans = 0
	else:
		n = (nmsum+nmdif)//2
		m = (nmsum-nmdif)//2
		if n<0 or m<0:
			ans = 0
		elif n==0 or m==0:
			ans = 1
		else:
			t = 1
			for i in range(1,n+m+1):
				t = (t*i)%mod
				if i==n: bb = t
				if i==m: cc = t
				if i==n+m: aa = t
			# aa = factorial(n+m)%mod
			# bb = factorial(n)%mod
			# cc = factorial(m)%mod
			ans = aa * modinv(bb,mod) %mod
			ans = ans * modinv(cc,mod) %mod

print(ans)