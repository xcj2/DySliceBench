import sys
input = sys.stdin.readline

def linput():
	return list(map(int,input().split()))

def pad(mxy, wall="#"):
	w = len(mxy[0])
	gp = wall*(w+2)
	re = [gp,]
	re_app = re.append
	for vx in mxy:
		re_app(wall+vx+wall)
	re_app(gp)
	return re

def main():
	H,W = linput()
	mM = [input().rstrip() for _ in [0,]*H]
	mM = pad(mM,".")
	mV = [[0,]*(W+2) for _ in [0,]*(H+2)]
	
	vD = [(0,1),(1,0)]
	
	res = False
	cnt = 0
	
	vQ = []
	vQ_app, vQ_pop = vQ.append, vQ.pop
	if mM[1][1]=="#":
		vQ_app((1,1))
	while vQ:
		x,y = vQ_pop()
		#print(x,y)
		if (x,y)==(W,H):
			res = True; mV[H][W] = 1; break
		
		
		t = 0
		for dx,dy in vD:
			nx,ny = x+dx, y+dy
			if mM[ny][nx]=="#" and \
			not mV[ny][nx]:
				t += 1
				vQ_app((nx,ny))
		
		if t>0:
			mV[y][x] = 1

		cnt += 1
		#print(res,cnt,X,Y,H)
		if cnt>999999: break
	
	if res:
		for vm,vv in zip(mM,mV):
			#print(vm,vv)#
			if not all(v for m,v in 
			  zip(vm,vv) if m=="#"):
				res = False; break
	
	print(("Impossible","Possible")[res])
	#print(res)

if __name__ == "__main__":
	main()
