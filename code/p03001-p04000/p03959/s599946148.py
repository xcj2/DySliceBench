import sys
input = sys.stdin.buffer.readline

#sys.setrecursionlimit(10**9)
#from functools import lru_cache

def RD(): return input().rstrip().decode()
def II(): return int(input())
def FI(): return float(input())
def MI(): return map(int,input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int,input().split()))
def LF(): return list(map(float,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode()


def main():
	n=II()
	T=LI()
	A=LI()

	X=[0]*n
	Y=[10**10]*n

	now=0
	for i,v in enumerate(T):
		if now<v:
			X[i]=v
			Y[i]=v
			now=v
		else:
			X[i]=max(X[i],1)
			Y[i]=min(Y[i],now)
	#print(X,Y)

	now=0
	for i,v in enumerate(reversed(A)):
		if now<v:
			if X[n-i-1]<=v<=Y[n-i-1]:
				X[n-i-1]=v
				Y[n-i-1]=v
			else:
				print(0)
				exit()
			now=v
		else:
			X[n-i-1]=max(X[n-i-1],1)
			Y[n-i-1]=min(Y[n-i-1],now)




	#print(X,Y)

	mod=10**9+7
	ans=1

	for i,j in zip(X,Y):
		if i>j:
			print(0)
			exit()
		else:
			ans*=(j-i+1)
			ans%=mod
	print(ans)










if __name__ == "__main__":
	main()
