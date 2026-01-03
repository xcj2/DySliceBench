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
	x=RD()

	ans=0
	s=0

	for i in x:
		if i=="S":
			s+=1
		else:
			if s==0:
				ans+=1
			else:
				s-=1

	print(ans+s)









if __name__ == "__main__":
	main()
