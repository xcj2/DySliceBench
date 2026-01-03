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
	n=II()
	x,y=1,1

	for _ in range(n):
		a,b=MI()
		k=max((x-1)//a,(y-1)//b)+1
		#print(k,x,y)
		x,y=k*a,k*b

	print(x+y)



if __name__ == "__main__":
	main()
