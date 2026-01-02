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
# rstrip().decode()

def main():
	n=II()
	A=LI()

	ans=1
	A.sort()
	for i in range(n):
		ans*=A[i]
		if ans>10**18:
			print(-1)
			exit(0)

	print(ans)


if __name__ == "__main__":
	main()
