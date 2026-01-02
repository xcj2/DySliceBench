import sys
input = sys.stdin.buffer.readline

#sys.setrecursionlimit(10**9)
#from functools import lru_cache

def RD(): return input().rstrip().decode()
def II(): return int(input())
def FI(): return int(input())
def MI(): return map(int,input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int,input().split()))
def LF(): return list(map(float,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode()

def main():
	n,k,c=MI()
	s=RD()

	A=[]
	now=0

	while now<n and len(A)<k:
		if s[now]=="o":
			A.append(now+1)
			now+=c+1
		else:
			now+=1
	#print(A)

	B=[]
	now=0
	while now<n and len(B)<k:
		if s[n-1-now]=="o":
			B.append(n-now)
			now+=c+1
		else:
			now+=1


	ans=[]
	for i,j in zip(A,B[::-1]):
		if i==j:
			ans.append(i)

	print(*ans,sep="\n")










if __name__ == "__main__":
	main()
