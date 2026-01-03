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
	s=input().rstrip().decode()

	n=len(s)

	for i in range(2,n,2):
		#print(s[:(n-i)//2])
		if s[:(n-i)//2]==s[(n-i)//2:n-i]:
			print(n-i)
			exit()













if __name__ == "__main__":
	main()
