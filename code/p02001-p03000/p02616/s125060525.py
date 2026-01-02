import sys
input = sys.stdin.buffer.readline


#sys.setrecursionlimit(10**9)
#from functools import lru_cache

def RD(): return sys.stdin.read()
def II(): return int(input())
def MI(): return map(int,input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int,input().split()))
def LF(): return list(map(float,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode()

#import numpy as np

def main():
	n,k=MI()
	A=LI()
	p=[]
	m=[]
	mod=10**9+7

	for i in A:
		if i>=0:
			p.append(i)
		else:
			m.append(i)
	p.sort(reverse=True)
	m.sort()
	#print(p,m)

	ans=1
	if (p==[] and k%2==1):
		for i in range(k):
			ans*=m[-i-1]
			ans%=mod
			#print(k,ans)

	elif n==k:
		for i in range(n):
			ans*=A[i]
			ans%=mod

	else:
		i=0
		j=0
		pl=len(p)
		ml=len(m)
		while k>=2:
			if i+2<=pl and j+2<=ml:
				pp=p[i]*p[i+1]
				mm=m[j]*m[j+1]
				if pp>mm:
					ans*=pp
					ans%=mod
					i+=2
				else:
					ans*=mm
					ans%=mod
					j+=2
			elif i+2<=pl:
				pp=p[i]*p[i+1]
				ans*=pp
				ans%=mod
				i+=2
			else:
				#print(i,j)
				mm=m[j]*m[j+1]
				ans*=mm
				ans%=mod
				j+=2
			k-=2

		if k==1:
			ans*=p[i]
			ans%=mod
	print(ans)



if __name__ == "__main__":
	main()
