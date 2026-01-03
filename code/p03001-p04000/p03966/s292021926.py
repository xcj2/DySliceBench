import sys
read = sys.stdin.buffer.read
input = sys.stdin.readline
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
# rstrip().decode('utf-8')


def main():
	n=II()
	a=1
	b=1

	for n in range(n):
		x,y=MI()
		if a<=x and b<=y:
			a,b=x,y
		elif a>x and b>y:
			t=max((a-1)//x,(b-1)//y)+1
			a,b=t*x,t*y
		elif a>x:
			t=(a-1)//x+1
			a,b=t*x,t*y
		else:
			t=(b-1)//y+1
			a,b=t*x,t*y

	print(a+b)





















if __name__ == "__main__":
	main()
