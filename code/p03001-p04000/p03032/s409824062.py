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
	V=LI()

	ans=0

	for a in range(min(n+1,k+1)):
		for b in range(min(n-a+1,k-a+1)):
			S=[]
			S+=V[:a]
			S+=V[n-b:]
			S.sort()
			tmp=sum(S)
			cnt=max(0,k-a-b)
			for i in range(min(a+b,cnt)):

				if S[i]<0:
					tmp-=S[i]
				else:
					break
			ans=max(ans,tmp)
	print(ans)










if __name__ == "__main__":
	main()
