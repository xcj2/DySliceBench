
# -*- coding: utf-8 -*-
def cf(x1,x2):
    cf=[]
    cf.append(1)
    for i in range(2,min(x1,x2)+1):
        if x1 % i == 0 and x2 % i == 0:
            cf.append(i)
    return cf

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def lcm(a, b):
	return a * b // gcd (a, b)

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

a, b = map(int, input().split())

result = factorization(gcd(a,b))
ans = len(result)
if not result[-1][0] == 1:
    ans += 1
print(ans)
