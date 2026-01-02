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


def main():
	n,k=MI()
	P=LI()
	for i in range(n):
		P[i]-=1
	C=LI()

	A=[[] for _ in range(n)]

	for i in range(n):
		A[i].append(C[i])
		now=P[i]
		while i!=now:
			A[i].append(A[i][-1]+C[now])
			now=P[now]
	#print(A)

	ans=-10**18

	for i in range(n):
		l=len(A[i])
		q,r=divmod(k-1,l)

		if q==0:
			ans=max(ans,max(A[i][:k]))
		else:
			if A[i][-1]<=0:
				ans=max(ans,max(A[i]))
			else:
				ans=max(ans,A[i][-1]*(q-1)+max(A[i]),A[i][-1]*(q)+max(A[i][:r+1]))

	print(ans)















if __name__ == "__main__":
	main()
