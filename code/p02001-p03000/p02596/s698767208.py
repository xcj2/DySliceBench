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
	k=II()
	a=0

	for i in range(k+10):
		b=pow(10,i,k)
		a+=7*b
		a%=k
		if a==0:
			print(i+1)
			exit()

	print(-1)





if __name__ == "__main__":
	main()
