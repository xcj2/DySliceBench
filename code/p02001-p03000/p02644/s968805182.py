import sys
read = sys.stdin.buffer.read
input = sys.stdin.readline
#input = sys.stdin.buffer.readline


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

from collections import deque

def main():
	h,w,k=MI()
	x1,y1,x2,y2=MI()
	G=["@"]*(w+2)
	for _ in range(h):
		G.append("@")
		G+=(list(map(str,input().rstrip())))
		G.append("@")
	G+=["@"]*(w+2)
	#print(G)


	G[x1*(w+2)+y1]=0
	#print(G)

	Q=deque()
	Q.append((x1*(w+2)+y1,0))

	while Q:
		#print(Q)
		now,d=Q.popleft()
		#print(Q)
		for m in [1,-1,w+2,-w-2]:
			for i in range(1,k+1):
				if G[now+m*i]==d or G[now+m*i]=="@":
					break
				elif G[now+m*i]==".":
					G[now+m*i]=d+1
					Q.append([now+m*i,d+1])
				elif G[now+m*i]==d+1:
					continue
				else:
					break

		#print(Q)
	#print(G)

	if G[x2*(w+2)+y2]==".":
		print(-1)
	else:
		print(G[x2*(w+2)+y2])


if __name__ == "__main__":
	main()
