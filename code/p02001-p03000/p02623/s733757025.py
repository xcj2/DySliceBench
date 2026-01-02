import sys
import math
from bisect import bisect_left
def II():
	return int(sys.stdin.readline())

def LI():
	return list(map(int, sys.stdin.readline().split()))

def MI():
	return map(int, sys.stdin.readline().split())

def SI():
	return sys.stdin.readline().strip()
def bs(a,n,x): 
    i = bisect_left(a, x) 
    if i<n and a[i] == x:
    	return i
    elif i:
    	return (i-1) 
    else: 
        return -1
n,m,k = MI()
a = LI()
b = LI()
for i in range(1,n):
	a[i]+=a[i-1]
for i in range(1,m):
	b[i]+=b[i-1]
ans = max(bs(a,n,k),bs(b,m,k))+1
for i in range(n):
	if k<a[i]:
		break
	else:
		temp = i+1+bs(b,m,k-a[i])+1
		ans = max(ans,temp)
for i in range(m):
	if k<b[i]:
		break
	else:
		temp = i+1+bs(a,n,k-b[i])+1
		ans = max(ans,temp)
print(ans)

