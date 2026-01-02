import sys
input = sys.stdin.readline
INF = 1001001001
from collections import deque

def linput(ty=int, cvt=list):
	return cvt(map(ty,input().split()))

def pad(mxy, wall="#"):
	w = len(mxy[0])
	gp = wall*(w+2)
	re = [gp,]
	re_app = re.append
	for vx in mxy:
		re_app(wall+vx+wall)
	re_app(gp)
	return re

vD = [(0,1),(1,0),(0,-1),(-1,0)]
vQ = deque([])
vQ_app, vQ_popl = vQ.append, vQ.popleft

def main():
	H,W = linput()
	mM = [input().rstrip() for _ in [0,]*H]
	mM = pad(mM,"$")
	
	res = 0
	cnt = 0
	
	mV = [[INF,]*(W+2) for _ in [INF,]*(H+2)]
	for sr in range(1,H+1):
		for sc in range(1,W+1):
			if mM[sr][sc]==".":
				continue
			mV[sr][sc] = 0
			vQ_app((sr,sc))
	
	while vQ:
		r,c = vQ_popl()
		now_cost = mV[r][c]
		for dr,dc in vD:
			nr,nc = r+dr, c+dc
			if mM[nr][nc]=="$":
				continue
			if now_cost + 1 < mV[nr][nc]:
				vQ_app((nr,nc))
				mV[nr][nc] = now_cost + 1
				res = max(now_cost+1, res)
		
		cnt += 1
		#print(res,cnt,X,Y,H)
		if cnt>4999999: break
	
	print(res)

if __name__ == "__main__":
	main()
