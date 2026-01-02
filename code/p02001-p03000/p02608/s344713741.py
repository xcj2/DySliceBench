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

	ans=[0]*(10**4+10)

	for x in range(1,105):
		for y in range(1,105):
			for z in range(1,105):
				a=x**2+y**2+z**2+x*y+y*z+z*x
				if a<=10**4:
					ans[a]+=1

	for i in range(1,n+1):
		print(ans[i])









if __name__ == "__main__":
	main()
