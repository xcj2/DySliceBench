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
	s=input().rstrip().decode()
	li=[0]*n
	
	q=II()
	K=LI()
	for k in K:
		D=0
		M=0
		DM=0
		ans=0
		
		for i in range(n):
			if s[i]=="D":
				D+=1
			elif s[i]=="M":
				M+=1
				DM+=D
			elif s[i]=="C":
				ans+=DM
			
			if i-k+1>=0:
				if s[i-k+1]=="D":
					D-=1
					DM-=M
				elif s[i-k+1]=="M":
					M-=1
		print(ans)
		


if __name__ == "__main__":
	main()
