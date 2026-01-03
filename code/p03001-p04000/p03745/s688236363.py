import sys
input = sys.stdin.readline
enum = enumerate

def linput(ty=int, cvt=list):
	return cvt(map(ty,input().split()))

def vinput(rep=1, ty=int, cvt=list):
	return cvt(ty(input().rstrip()) for _ in "*"*rep)

def gcd(a: int, b: int):
	while b: a, b = b, a%b
	return a

def lcm(a: int, b: int):
	return a * b // gcd(a, b)

def main():
	N = int(input())
	vA = linput()
	#vA.sort()
	#vA.reverse()
	
	if N==1:
		print(1)
		return
		
	vC =[a-pp for a,pp in zip(vA[1:],vA)]
		
	res = 0
	pp = 0
	cnt = 0
	for c in vC:
		if c==0: continue
		if pp==0:
			pp = 1 if c>0 else -1
			cnt = 1
			res += 1
			continue
		if c>0 and pp<0:
			cnt = 1
			pp = 0
			continue
		if c<0 and pp>0:
			cnt = 1
			pp = 0
			continue
		cnt += 1
	
	if pp==0:
		res += 1
	#sT = "No Yes".split()
	#print(sT[res])
	print(res)

if __name__ == "__main__":
	main()
