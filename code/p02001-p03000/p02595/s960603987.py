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
	n,d=MI()
	d=d**2

	ans=0

	for _ in range(n):
		x,y=MI()
		if x**2+y**2<=d:
			ans+=1

	print(ans)





if __name__ == "__main__":
	main()
