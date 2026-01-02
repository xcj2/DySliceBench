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
	A=LI()
	B=LI()
	pos=0
	neg=0

	for i,j in zip(A,B):
		if j-i>=0:
			pos+=(j-i)//2
		else:
			neg+=-j+i
	if pos>=neg:
		ans="Yes"
	else:
		ans="No"

	print(ans)






if __name__ == "__main__":
	main()
