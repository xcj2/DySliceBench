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
	n,d=MI()
	X=[LI() for _ in range(n)]
	#print(X)
	ans=0

	for i in range(n-1):
		for j in range(i+1,n):
			k=0
			for x,y in zip(X[i],X[j]):
				k+=(x-y)**2
			#print(k)
			if k**0.5==int(k**0.5):
				ans+=1

	print(ans)








if __name__ == "__main__":
	main()
