import sys
input = sys.stdin.buffer.readline

#sys.setrecursionlimit(10**9)
#from functools import lru_cache

def RD(): return input().rstrip().decode()
def II(): return int(input())
def FI(): return float(input())
def MI(): return map(int,input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int,input().split()))
def LF(): return list(map(float,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode()



def main():
	n,m=MI()
	x=LI()
	x.sort()
	A=[]
	for i,j in zip(x[1:],x[:-1]):
		A.append(i-j)
	#print(A)
	A.sort()
	print(sum(A[:max(m-n,0)]))


if __name__ == "__main__":
	main()
