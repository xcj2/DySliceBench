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


#import numpy as np

def main():
	x,y,a,b,c=MI()
	p=LI()
	q=LI()
	r=LI()

	p.sort()
	q.sort()
	r.sort()

	p=p[a-x:]
	q=q[b-y:]

	li=p+q+r
	li.sort()
	li=li[len(li)-x-y:]
	print(sum(li))




if __name__ == "__main__":
	main()