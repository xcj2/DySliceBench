import sys
bbn=1000000007
	
#+++++


def mkm2(a_ll):
	ccc=0
	for i, c in enumerate(a_ll):
		ccc += ((-2)**i)*(c==1)
	return ccc

def show(a_ll):
	ret = ''.join([str(i) for i in a_ll[::-1]])
	return ret


def main():
	a = int(input())
	if a == 0:
		return 0
	a=-a
	
	ret=[]
	while mkm2(ret) < a and False:
		ret.append(0)
		ret.append(1)
		pa(mkm2(ret))
		pa(ret)
	
	while a != 0:
		if a %(-2)==0:
			ret.append(0)
		else:
			ret.append(1)
		a = a // (-2)
		
	pa(mkm2(ret))
	print(show(ret))
	
	
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