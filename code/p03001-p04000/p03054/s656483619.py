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


def main():
	h,w,n=MI()
	sr,sc=MI()
	S=RD()
	T=RD()

	ans="YES"

	#Rの検証
	x=w-sc+1
	for i,j in zip(S,T):
		if i=="R":
			x-=1
			if x==0:
				ans="NO"
		if j=="L":
			if x<w:
				x+=1

	#Lの検証
	x=sc
	for i,j in zip(S,T):
		if i=="L":
			x-=1
			if x==0:
				ans="NO"
		if j=="R":
			if x<w:
				x+=1

	#Dの検証
	x=h-sr+1
	for i,j in zip(S,T):
		if i=="D":
			x-=1
			if x==0:
				ans="NO"
		if j=="U":
			if x<h:
				x+=1

	#Uの検証
	x=sr
	for i,j in zip(S,T):
		if i=="U":
			x-=1
			if x==0:
				ans="NO"
		if j=="D":
			if x<h:
				x+=1

	print(ans)










if __name__ == "__main__":
	main()
