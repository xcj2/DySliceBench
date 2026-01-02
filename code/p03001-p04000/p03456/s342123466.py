import sys

#+++++

def ic(dd):
	if dd == 0:
		return True
	if dd == 1:
		return True
	
	for i in range(dd):
		if i ** 2 == dd:
			return True
			
		if i ** 2 > dd:
			return False
			
	return False

def main():
	b , c = map(int, input().split())
	dd = int(str(b)+str(c))
	r=ic(dd)
	ret = 'Yes' if r else 'No'

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