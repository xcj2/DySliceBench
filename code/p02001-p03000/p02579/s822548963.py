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

from collections import deque

def main():
	h,w=MI()
	ch,cw=MI()
	dh,dw=MI()
	ch+=1
	cw+=1
	dh+=1
	dw+=1

	S=[["#"]*(w+4)]
	S.append(["#"]*(w+4))
	for _ in range(h):
		S.append(["#"]*2+list(RD())+["#"]*2)
	S.append(["#"]*(w+4))
	S.append(["#"]*(w+4))

	#print(S)

	S[ch][cw]=0
	Q=deque()
	Q.append([0,ch,cw])


	d1=[(0,1),(0,-1),(-1,0),(1,0)]
	d2=[(i,j) for i in range(-2,3) for j in range(-2,3)]

	while Q:
		#print(Q)
		d,x,y=Q.popleft()

		for xx,yy in d1:
			if S[x+xx][y+yy]==".":
				S[x+xx][y+yy]=d
				Q.appendleft([d,x+xx,y+yy])
			elif S[x+xx][y+yy]=="#":
				continue
			elif S[x+xx][y+yy]>d:
				S[x+xx][y+yy]=d
				Q.appendleft([d,x+xx,y+yy])

		for xx,yy in d2:
			if S[x+xx][y+yy]==".":
				S[x+xx][y+yy]=d+1
				Q.append([d+1,x+xx,y+yy])
			elif S[x+xx][y+yy]=="#":
				continue
			elif S[x+xx][y+yy]>d+1:
				S[x+xx][y+yy]=d+1
				Q.appendleft([d+1,x+xx,y+yy])



	#print(S[2:-2])

	print(-1 if S[dh][dw]=="." else S[dh][dw])


if __name__ == "__main__":
	main()
