import math

def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
 
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)
 

def f(b,n):
	if n < b:
		return n
	return f(b, n//b) + n%b
 

N, K = map(int,input().split())
v = list(map(int,input().split()))
bubunwa = [0]

for i in range(len(v)):
	bubunwa.append(v[i]+bubunwa[-1])

sums = []
for i in range(len(bubunwa)-1):
	for j in range(i+1, len(bubunwa)):
		sums.append(bubunwa[j]-bubunwa[i])

ans = 0
good = []
for i in range(40,-1,-1):

	bit = 1 << i

	for elem in sums:
		if elem & bit == bit:
			good.append(elem)

	if len(good) >= K:
		ans += bit
		sums = good
		good = []
	else:
		good = []

print(ans)