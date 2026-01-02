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
	n,k=MI()
	li=[LI() for _ in range(n)]
	#print(li)

	ans=10**20

	X=[]
	Y=[]

	for x,y in li:
		X.append(x)
		Y.append(y)
	X.sort()
	Y.sort()
	#print(X,Y)

	for i in range(n):
		for ii in range(i+1,n):
			for j in range(n):
				for jj in range(j+1,n):
					cnt=0
					for x,y in li:
						if X[i]<=x<=X[ii] and Y[j]<=y<=Y[jj]:
							cnt+=1
					#print(i,ii,j,jj,X[i],X[ii],Y[j],Y[jj],cnt,ans)
					if cnt>=k:
						ans=min(ans,(X[ii]-X[i])*(Y[jj]-Y[j]))

	print(ans)












if __name__ == "__main__":
	main()
