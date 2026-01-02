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

def main():
	n=II()
	A=LI()
	A.append(0)

	L=[]
	R=[]

	f=0
	now=200
	i=0
	while i<n+1:
		if f==0:
			if A[i]<=now:
				now=A[i]
				i+=1
			else:
				L.append(now)
				f=1
		else:
			if A[i]>=now:
				now=A[i]
				i+=1
			else:
				R.append(now)
				f=0

	#print(L,R)

	ans=1000

	for i,j in zip(L,R):
		q,r=divmod(ans,i)
		ans=q*j+r
	print(ans)





















if __name__ == "__main__":
	main()
