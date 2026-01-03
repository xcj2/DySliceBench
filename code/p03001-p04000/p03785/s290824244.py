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
	#i = 0   #..N
	cnt = 0 #..C
	x = 0   #(T-x)..K
	
	for a in vA:
		if a<=x and cnt<C:
			cnt += 1
			continue
		cnt = 1
		res += 1
		x = a+K
	
	#sT = "No Yes".split()
	#print(sT[res])
	print(res)

if __name__ == "__main__":
	main()
