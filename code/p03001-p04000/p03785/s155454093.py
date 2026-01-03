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
	N,C,K = linput()
	vA = vinput(N)
	vA.sort()
	#vA.reverse()
	
	res = 0
	i = 0   #..N
	cnt = 0 #..C
	x = 0   #(T-x)..K
	while i<len(vA):
		if not cnt:
			cnt += 1
			x = vA[i]+K
			i += 1
			res += 1
		elif cnt<C:
			if vA[i]<=x:
				cnt += 1
				i += 1
			else:
				cnt = 1
				x = vA[i]+K
				res += 1
				i += 1
		else:
			cnt = 1
			x = vA[i]+K
			res += 1
			i += 1
	
	#sT = "No Yes".split()
	#print(sT[res])
	print(res)

if __name__ == "__main__":
	main()
