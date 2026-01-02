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

import bisect
from collections import defaultdict

def main():
	s=RD()
	t=RD()
	d=defaultdict(list)

	for i,ss in enumerate(s):
		d[ss].append(i)
	#print(d)

	now=-1
	cnt=0

	for tt in t:
		if d[tt]==[]:
			print(-1)
			exit()
		else:
			i=bisect.bisect_right(d[tt],now)
			if len(d[tt])==i:
				cnt+=1
				now=d[tt][0]
			else:
				now=d[tt][i]
		#print(tt,i,now,cnt)
	print(len(s)*cnt+now+1)

























if __name__ == "__main__":
	main()
