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
			
	vC =[a-pp for a,pp in zip(vA[1:],vA)
		 if a!=pp]
		
	res = 0
	pp = 0

	for c in vC:
		if pp==0:
			pp = 1 if c>0 else -1
			res += 1
		if c*pp<0:
			pp = 0
	
	if pp==0:
		res += 1
	#sT = "No Yes".split()
	#print(sT[res])
	print(res)

if __name__ == "__main__":
	main()
