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
	x,n=MI()
	p=[]
	if n!=0:
		p=LI()
	p.sort()

	diff=105
	ans=105

	for i in range(105,-1,-1):
		if i in p:
			continue
		else:
			if abs(i-x)<=diff:
				ans=i
				diff=abs(i-x)

	print(ans)













if __name__ == "__main__":
	main()
