import sys
import itertools
bbn=1000000007
	
#+++++

def iii(a,b):
	for i,j in zip(a,b):
		if i != j:
			return False
	return True
		
def main():
	n = int(input())
	al = list(map(int, input().split()))
	bl = list(map(int, input().split()))
	cl=al[:]
	cl.sort()
	p=0
	q=0
	i=0
	for ii in itertools.permutations(cl):
		i+=1
		if iii(ii, al):
			p=i
		if iii(ii,bl):
			q=i
		
	print(abs(p-q))
	
	
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