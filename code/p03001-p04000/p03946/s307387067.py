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
	n,t=MI()
	A=LI()

	B=[A[0]]
	for i in A[1:]:
		B.append(min(B[-1],i))
	#print(B)

	C=[0]*n

	for i in range(n):
		C[i]=A[i]-B[i]

	c=max(C)
	print(C.count(c))

	
	



	
	
	









if __name__ == "__main__":
	main()
