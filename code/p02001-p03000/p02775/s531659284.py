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
	n=RD()[::-1]
	N=list(map(int,n))+[0]
	#print(N)

	ans=0

	for i in range(len(n)+1):
		if N[i]<=4:
			ans+=N[i]
		elif N[i]>=6:
			ans+=10-N[i]
			N[i+1]+=1
		else:
			if N[i+1]<=4:
				ans+=N[i]
			else:
				ans+=N[i]
				N[i+1]+=1

	print(ans)









if __name__ == "__main__":
	main()
