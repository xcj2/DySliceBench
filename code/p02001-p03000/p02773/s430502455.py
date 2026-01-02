import sys
from collections import defaultdict

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
mod=1000000007

#+++++

def main():
	n = int(input())
	dd=defaultdict(lambda :0)
	for i in range(n):
		s = input()
		dd[s]+=1
		
	maxv=0
	mml=[]
	for k in dd.keys():
		if dd[k]==maxv:
			mml.append(k)
		elif dd[k]>maxv:
			maxv=dd[k]
			mml=[k]
		else:
			pass
			
	mml.sort()
	for k in mml:
		print(k)
	
	
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