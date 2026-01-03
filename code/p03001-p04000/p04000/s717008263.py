import sys
from collections import defaultdict

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(IN())
mod=1000000007

#+++++

def main():
	#a = int(input())
	H, W, N = tin()
	#s = input()
	dd=defaultdict(lambda : 0)
	for _ in range(N):
		a, b = tin()
		for da in range(3):
			for db in range(3):
				if a - da <= 0 or b - db <= 0:
					continue
				if a - da > H -2 or b -db > W-2:
					continue
				ii = (a - da)*(W+1)+(b - db)
				dd[ii]+=1
	
	nn = [0]*10
	for k in dd:
		nn[dd[k]]+=1
	nn[0]=((H-2)*(W-2))-sum(nn[1:])
	for v in nn:
		print(v)
	
	
	
#+++++
isTest=False

def pa(v):
	if isTest:
		print(v)
		
def input_clipboard():
	import clipboard
	input_text=clipboard.get()
	input_l=input_text.splitlines()
	for l in input_l:
		yield l

if __name__ == "__main__":
	if sys.platform =='ios':
		if input_method==input_methods[0]:
			ic=input_clipboard()
			input = lambda : ic.__next__()
		elif input_method==input_methods[1]:
			sys.stdin=open('inputFile.txt')
		else:
			pass
		isTest=True
	else:
		pass
		#input = sys.stdin.readline
			
	ret = main()
	if ret is not None:
		print(ret)