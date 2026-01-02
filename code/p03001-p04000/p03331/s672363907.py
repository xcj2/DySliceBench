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
	n=II()

	ans=10**10


	for i in range(1,n):
		a=str(i)
		b=str(n-i)
		cnt=0
		for aa in a:
			cnt+=int(aa)
		for bb in b:
			cnt+=int(bb)
		ans=min(ans,cnt)
	print(ans)









if __name__ == "__main__":
	main()
