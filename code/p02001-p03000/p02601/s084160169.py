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
	a,b,c=MI()
	k=II()

	while b<=a:
		b*=2
		k-=1

	while c<=b:
		c*=2
		k-=1

	#print(a,b,c,k)

	if k>=0:
		ans="Yes"
	else:
		ans="No"

	print(ans)






if __name__ == "__main__":
	main()
