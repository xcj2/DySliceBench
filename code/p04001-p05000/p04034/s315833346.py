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
	n,m=MI()
	A=[1]*(n+1)
	ans=[0]*(n+1)
	ans[1]=1

	for _ in range(m):
		x,y=MI()
		if ans[x]==1:
			ans[y]=1
		if A[x]==1 and ans[x]==1:
			ans[x]=0
		A[x]-=1
		A[y]+=1
		#print(A,ans)

	print(sum(ans))









if __name__ == "__main__":
	main()
