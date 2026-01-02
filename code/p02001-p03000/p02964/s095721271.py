import sys
input = sys.stdin.buffer.readline

#sys.setrecursionlimit(10**9)
#from functools import lru_cache

def RD(): return input().rstrip().decode()
def II(): return int(input())
def FI(): return int(input())
def MI(): return map(int,input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int,input().split()))
def LF(): return list(map(float,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode()

import bisect

def main():
	n,k=MI()
	A=LI()
	B=[[] for _ in range(2*10**5+10)]

	for i,v in enumerate(A):
		B[v-1].append(i)

	for li in B:
		if li:
			li.append(li[0])

	#print(A)
	#print(B)

	C=[]

	s=0
	t=-1

	while t<n-1:
		a=A[s]-1
		ti=bisect.bisect_left(B[a][:-1],s)+1
		t=B[a][ti]
		#print(s,t)
		if s>=t:
			C.append(s)
		s=t+1
	#print(C)

	k%=len(C)+1
	#print(k)

	if k==0:
		print()
		exit()

	s=C[k-1]
	#print(s)

	ans=[]

	while s<n:
		a=A[s]-1
		si=bisect.bisect_left(B[a][:-1],s)
		if si+1==len(B[a][:-1]):
			ans.append(a+1)
			s+=1
		else:
			s=B[a][si+1]+1
	print(*ans)



if __name__ == "__main__":
	main()
