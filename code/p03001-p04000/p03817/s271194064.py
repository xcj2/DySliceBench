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
	x=II()
	q,r=divmod(x,11)
	ans=0
	if r==0:
		ans-=1


	ans+=2*q+1+(r>6)

	print(ans)


if __name__ == "__main__":
	main()
