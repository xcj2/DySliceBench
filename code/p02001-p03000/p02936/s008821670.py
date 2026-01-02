import sys
input = sys.stdin.readline
input = sys.stdin.buffer.readline
def RD(): return sys.stdin.read()
def II(): return int(input())
def MI(): return map(int,input().split())
def LI(): return list(map(int,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode('utf-8')
#import numpy as np

from collections import deque

def main():
	n,q=MI()
	E=[[] for _ in range(n+1)]
	X=[0]*(n+1)

	for _ in range(n-1):
		a,b=MI()
		E[a].append(b)
		E[b].append(a)
	for _ in range(q):
		p,x=MI()
		X[p]+=x
	#print(E)

	Q=deque([1])

	while Q:
		#print(Q)
		now=Q.popleft()
		#print(now)
		if E[now]!=[]:
			for i in E[now]:
				if E[i]!=[]:
					Q.append(i)
					X[i]+=X[now]
			E[now]=[]
	print(*X[1:])


if __name__ == "__main__":
	main()