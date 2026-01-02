import sys
input = sys.stdin.readline

def linput(ty=int, cvt=list):
	return cvt(map(ty,input().split()))

def gcd(a: int, b: int):
	while b: a, b = b, a%b
	return a

def lcm(a: int, b: int):
	return a * b // gcd(a, b)

def main():
	D = int(input())  # days
	vC = [0,]+linput()     # decrine rate
	
	#sumC = sum(vC)
	
	# satis (d,i)
	mS = [[0,]+linput() for _ in [0,]*D]
	
	## sample output
	#vT = [int(input()) for _ in [0,]*D] ## for p.B

	vL = [-1,]*(26+1)   # last day of Type
	
	#day = -1
	res = 0      # manzoku
	vR = []
	vT = []
	rapp = vR.append
	tapp = vT.append
	
	for d in range(D): #[0,364] day
		#t = vT[d] ## sample output
		bestT = 1
		candiR = []
		vS = mS[d]
		for t in range(1,27):  # [1,26] type
			candir = 0
			Sdt = vS[t]
			candir += Sdt
			
			vltmp = vL[t]
			vL[t] = d
			C = sum(c*(d-l) for c,l in zip(vC,vL))
			candir -= C
			candiR.append(candir)
			
			vL[t] = vltmp
		
		bestR = max(candiR)
		bestT = candiR.index(bestR) + 1
		res += bestR
		rapp(res)
		tapp(bestT)
	
	#sT = "No Yes".split()
	#print(sT[res])
	#print(res)
	print(*vT, sep='\n')
	print(*vR, file=sys.stderr)
	print(sum(vR), file=sys.stderr)

if __name__ == "__main__":
	main()
