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
	n,k=MI()


	a=0
	b=0
	for i in range(1,n+1):
		if i%k==0:
			a+=1

	if k%2==0:
		for i in range(1,n+1):
			if i%(k//2)==0:
				b+=1
		b-=a
	#print(a,b)

	print(a**3+b**3)











if __name__ == "__main__":
	main()
