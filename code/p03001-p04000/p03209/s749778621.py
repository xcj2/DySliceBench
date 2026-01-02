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
 
N,X = map(int,input().split())
X-=1

P = [0,1]

for i in range(1,N):
    P.append(P[i]*2+1)

left = 0
right = 1
for i in range(N):
    right = right*2 + 3

mid = int((right-left)/2)
ans = 0

while(left <= right):
    if(X<mid):
        right = mid-1
        left += 1
        N-=1
    elif (X>mid):
        left = mid+1
        right -= 1
        ans = ans + P[N] + 1
        N-=1
    else:
        ans = ans + P[N] + 1
        break

    mid = left+int((right-left)/2)
    
print(ans)