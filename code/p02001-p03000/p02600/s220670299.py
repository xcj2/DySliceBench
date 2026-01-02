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
	x=II()

	if x<600:
		a=8
	elif x<800:
		a=7
	elif x<1000:
		a=6
	elif x<1200:
		a=5
	elif x<1400:
		a=4
	elif x<1600:
		a=3
	elif x<1800:
		a=2
	elif x<2000:
		a=1
	print(a)

if __name__ == "__main__":
	main()
