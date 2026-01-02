import sys
input = sys.stdin.readline
INF = 1001001001
from collections import deque

def linput(ty=int, cvt=list):
	return cvt(map(ty,input().split()))

def pad(mxy, w="#"):
	gp = w*(len(mxy[0])+2)
	return [gp,]+[w+vx+w for vx in mxy]+[gp,]

vD = [(0,1),(1,0),(0,-1),(-1,0)]
vQ = deque([])
vQ_app, vQ_popl = vQ.append, vQ.popleft

def main():
	H,W = linput()
	sr,sc = 1,1
	gr,gc = H,W
	mM = [input().rstrip() for _ in "*"*H]
	walls = sum(s.count("#") for s in mM)
	mM = pad(mM,"#")
	#print(mM)#
	
	res = 0
	cnt = 0
	
	mV = [[INF,]*(W+2) for _ in "*"*(H+2)]
	#for sr in range(1,H+1):
	#	for sc in range(1,W+1):
	#		if mM[sr][sc]==".":
	#			continue
	mV[sr][sc] = 0
	vQ_app((sr,sc))
	
	while vQ:
		r,c = vQ_popl()
		now_cost = mV[r][c]
		for dr,dc in vD:
			nr,nc = r+dr, c+dc
			if mM[nr][nc]!=".":
				continue
			if now_cost + 1 < mV[nr][nc]:
				vQ_app((nr,nc))
				mV[nr][nc] = now_cost + 1
				#res = max(now_cost+1, res)
		
		cnt += 1
		#print(res,cnt,X,Y,H)
		if cnt>4999999: break
	
	res = mV[gr][gc]
	if res == INF:
		res = -1
	else:
		res = H*W - res - walls - 1
	print(res)

if __name__ == "__main__":
	main()
