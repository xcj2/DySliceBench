import sys
bbn=1000000007
	
#+++++

def modinv(a,m):
	b=m
	u=1
	v=0
	
	while b > 0:
		t = a //b
		a = a - (t * b)
		a,b = b,a
		u = u - (t * v)
		u,v=v,u
	
	u = u % m
	if u < 0:
		u+=m
	return u

def gcd(a,b):
	while b!= 0:
		a,b=b,a%b
		
	return a
		
def main():
	n = int(input())
	al = list(map(int, input().split()))
	
	#saisyoukoubausuu
	ss=1
	for v in al:
		ss = ss * v //gcd(ss,v)
		#ss %= bbn
	
	ss=ss%bbn
	ret=0
	for v in al:
		ret += ss *modinv(v, bbn)
		ret%=bbn
		
	
	print(ret)
	
	
#+++++
isTest=False

def pa(v):
	if isTest:
		print(v)

if __name__ == "__main__":
	if sys.platform =='ios':
		sys.stdin=open('inputFile.txt')
		isTest=True
	else:
		pass
		#input = sys.stdin.readline
			
	ret = main()
	if ret is not None:
		print(ret)