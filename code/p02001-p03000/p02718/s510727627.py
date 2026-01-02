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
	n,m=MI()
	A=LI()
	A.sort(reverse=True)
	S=sum(A)


	ans="Yes"

	for i in range(m):
		if A[i]*4*m<S:
			ans="No"
			break

	print(ans)
















if __name__ == "__main__":
	main()
