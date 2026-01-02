import sys
input = sys.stdin.readline
#input = sys.stdin.buffer.readline

#sys.setrecursionlimit(10**9)

def RD(): return sys.stdin.read()
def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode('utf-8')
#import numpy as np

from collections import deque

def main():
	h,w=MI()
	G=["#"]*(w+2)
	for i in range(h):
		G+=["#"]+list(input().rstrip())+["#"]
	G+=["#"]*(w+2)
	ans=0
	#print(G)
	for i in range((h+2)*(w+2)):
		if G[i]==".":
			ans+=1

	Q=deque()
	Q.append((w+3,1))
	G[w+3]="#"
	f=0
	while Q:
		#print(Q)
		x,d=Q.popleft()
		if x==(w+2)*(h+2)-(w+2)-2:
			f=1
			break
		for dx in [-1,1,-w-2,w+2]:
			if G[x+dx]==".":
				Q.append((x+dx,d+1))
				G[x+dx]="#"

	if f==1:
		print(ans-d)
	else:
		print(-1)


























































if __name__ == "__main__":
	main()