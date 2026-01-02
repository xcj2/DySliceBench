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
 

s = input().strip()
ans = int(s[0])*100+int(s[1])*10+int(s[2])

for i in range(1, len(s)-2):
    if(abs(int(s[i])*100+int(s[i+1])*10+int(s[i+2]) - 753) < abs(ans - 753)):
        ans = int(s[i])*100+int(s[i+1])*10+int(s[i+2])

print(abs(753-ans))