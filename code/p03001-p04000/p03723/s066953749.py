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
	a,b,c = linput()
	d = a-b
	res = 0

	cnt = 0
	while cnt<10**2:
		if a%2 or b%2 or c%2:
			break
		p,q,r = a//2, b//2, c//2
		s = p+q+r
		a,b,c = s-p, s-q, s-r
		cnt += 1
		#print(a,b,c)
	else:
		cnt = -1
	
	res = cnt
	#sT = "No Yes".split()
	#print(sT[res])
	print(res)

if __name__ == "__main__":
	main()
