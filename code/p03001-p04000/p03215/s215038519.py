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
	n,k=MI()
	A=LI()
	B=[0]
	C=[0]

	for i in A:
		B.append(B[-1]+i)
		C.append(C[-1]^i)
	#print(A,B,C)


	ans=0

	D=[]
	E=[]
	F=[]

	for i in range(n):
		for j in range(i+1,n+1):
			D.append(B[j]-B[i])

	#print(D)

	ans=0

	for i in range(41,-1,-1):
		cnt=0
		E=[]
		for d in D:
			if 1<<i&d:
				E.append(d)
				cnt+=1
				#print(1<<i,d)

		if cnt>=k:
			ans+=1<<i
			D=E.copy()

	print(ans)
	
	









if __name__ == "__main__":
	main()
