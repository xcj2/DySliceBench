import math
 
def prime_factors(n):
	i = 2
	factors = []
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
			factors.append(i)
	if n > 1:
		factors.append(n)
	return factors
	

def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)
		
def modinv(a, m):
	g, x, y = egcd(a, m)
	if g != 1:
		raise Exception('modular inverse does not exist')
	else:
		return x % m
		
def factorial(n):
	num = 1
	while n >= 1:
		num = (num * n) % 1000000007
		n = n - 1
	return num
	   
a = input().split()
a = [int(i) for i in a]
 
num = dict()
for i in prime_factors(a[1]):
	if i not in num:
		num[i] = 1
	else:
		num[i] += 1
		
ans = 1
for j in num.values():
	ans *= factorial(j + a[0] - 1)
	ans %= (10**9 + 7)
	inv = modinv((factorial(a[0] - 1)* factorial(j)), 1000000007)
	ans *= inv
	ans %= (10**9 + 7)
	
print(ans)