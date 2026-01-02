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
	n=II()

	ans=0
	for i in range(1,10**6+10):
		a=n-i
		if a%i==0:
			b=a//i
			if b>i:
				ans+=b
			else:
				break
	print(ans)



	
	
	



	
	
	









if __name__ == "__main__":
	main()
