import sys

#+++++
	
def gcd(a,b):
	if a < b:
		a,b = b,a
	
	while b!=1:
		tt=a%b
		if tt==0:
			return b
		a,b=b,tt
		
	return b
	
def is_sosuu(v, pl):
	if v == 2:
		return True
	if v <= 1:
		return False
	for p in pl:
		if v %p==0:
			return False
	return True
	
def bbb(val):
	return int(val**(0.5))+1
	
def main():
	b , c = map(int, input().split())
	sk=gcd(b,c)
	
	#素因数分解。素数の数+1を出力
	ans=1
	sosuu_list=[]
	using=set()
	using.add(1)
	sss=sk
	for i in range(2,bbb(sss)+1):
		while sss % i == 0:
			sss = sss // i
			using.add(i)
			if bbb(sss) < i:
				using.add(sss)
				break
	using.add(sss)
	print(len(using))
	
	
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