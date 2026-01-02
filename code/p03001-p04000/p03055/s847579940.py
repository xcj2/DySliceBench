import sys
read = sys.stdin.buffer.read
input = sys.stdin.readline
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
# rstrip().decode('utf-8')

from collections import deque

def main():
	n=II()
	G=[[] for _ in range(n+1)]
	
	for _ in range(n-1):
		a,b=MI()
		G[a].append(b)
		G[b].append(a)
	#print(G)
	
	Q=deque()
	Q.append([1,0])
	l=0
	v=0
	sumi=set()
	
	while Q:
		#print(Q)
		now,d=Q.popleft()
		sumi.add(now)
		if d>l:
			v=now
			l=d
		for i in G[now]:
			if i not in sumi:
				Q.append([i,d+1])
	#print(v,l)
	
	Q=deque()
	Q.append([v,0])
	l=0
	sumi=set()
	while Q:
		#print(Q)
		now,d=Q.popleft()
		sumi.add(now)
		if d>l:
			l=d
		for i in G[now]:
			if i not in sumi:
				Q.append([i,d+1])
	#print(l)
	
	if l%3==1:
		print("Second")
	else:
		print("First")

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	









if __name__ == "__main__":
	main()
