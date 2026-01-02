import sys
bbn=1000000007
	
#+++++

def ai(n, c):
	if n <= 9550:
		bb=1	
		ret=0
		while n >= 10**bb:
			ret += n // 10**bb
			bb+=1
		return ret+c
	else:
		p=0
		b=n
		while b % 10 == 0:
			p+=1
			b=b//10
		return ai(n-2, c+p)
		
def main():
	n = int(input())
	if n%2==1:
		return 0
	bb=1	
	ret=0
	while n >= 2*(5**bb):
		ret += n // (2*(5**bb))
		bb+=1
	#pa(ai(n,0))
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