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
	A=LI()
	A.sort()
	A.append(10**7)
	li=[0]*(10**6+10)

	ans=0
	f=0
	for k in range(n):
		i=A[k]
		if i==A[k+1]:
			f=1
			continue
		if li[i]==0:
			if f==0:
				ans+=1
			j=1
			while i*j<10**6+5:
				li[i*j]=1
				j+=1
		f=0

	print(ans)
















if __name__ == "__main__":
	main()
