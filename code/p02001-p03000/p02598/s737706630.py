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
	A=LI()


	l=1
	r=max(A)+10

	while l+1<r:
		m=(l+r)//2
		cnt=0

		for i in A:
			cnt+=(i-1)//(m-1)
		#print(l,m,r,cnt)
		if cnt<=k:
			r=m
		else:
			l=m



	print(l)
















if __name__ == "__main__":
	main()
