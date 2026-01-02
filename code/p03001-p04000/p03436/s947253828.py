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

from collections import deque

def main():
	h,w=MI()
	G=[]
	G+=["#"]*(w+2)
	for _ in range(h):
		G+=["#"]+list(RD())+["#"]
	G+=["#"]*(w+2)

	cnt=G.count(".")


	Q=deque()
	Q.append([w+3,1])
	G[w+3]=1

	while Q:
		now,d=Q.popleft()
		for i in [1,-1,w+2,-w-2]:
			if G[now+i]==".":
				G[now+i]=d+1
				Q.append([now+i,d+1])

	ans=-1
	if G[(w+2)*(h+2)-(w+4)]!=".":
		ans=cnt-G[(w+2)*(h+2)-(w+4)]

	print(ans)












if __name__ == "__main__":
	main()
