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
	n=II()
	A=[0]+LI()
	B=[0]*(n+1)

	for i in range(n,0,-1):
		a=A[i]
		if n//i>=2:
			for j in range(2,n//i+1):
				#print(i,j)
				a^=B[i*j]
		B[i]=a

	ans=[]
	for i,v in enumerate(B):
		if v:
			ans.append(i)

	print(len(ans))
	print(*ans)













if __name__ == "__main__":
	main()
