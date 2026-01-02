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

from itertools import permutations


def main():
	n=II()
	P=TI()
	Q=TI()
	ans=0
	for i,p in enumerate(permutations(range(1,n+1),n)):
		if P==p:
			ans-=i
		if Q==p:
			ans+=i
	print(abs(ans))




if __name__ == "__main__":
	main()
