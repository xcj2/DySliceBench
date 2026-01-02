import sys
input = sys.stdin.readline
INF = 99999#1001001001
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

vD = [(0,1),(1,0)]
vQ = deque([])
vQ_app, vQ_popl = vQ.append, vQ.popleft

def main():
	H,W = linput()
	mM = [input().rstrip() for _ in [0,]*H]
	mM = pad(mM, "$")
	
	res = 0
	cnt = 0
	
	for sr in range(1,1+1):
		for sc in range(1,1+1):
			if mM[sr][sc]=="#":
				res += 1
			mV = [[INF,]*(W+2) for _ in [INF,]*(H+2)]
			mV[sr][sc] = res
			vQ_app((sr,sc))
			while vQ:
				r,c = vQ_popl()
				now_cost = mV[r][c]
				now_s = mM[r][c]
				for dr,dc in vD:
					nr,nc = r+dr, c+dc
					if mM[nr][nc]=="$":
						continue
					next = now_s=="."!=mM[nr][nc]
					new_cost = now_cost + next
					if new_cost < mV[nr][nc]:
						vQ_app((nr,nc))
						mV[nr][nc] = new_cost
		
				cnt += 1
				#print(res,cnt,X,Y,H)
				if cnt>999999: break
	
	#print(*mV,sep="\n")###
	res = mV[H][W]
	print(res)

if __name__ == "__main__":
	main()
