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
	al = list(IN())
	vv=defaultdict(lambda : 0)
	for v in al:
		vv[v]+=1
	
	dd=dict()
	total=0
	for key in vv:
		num=vv[key]
		use_all = num*(num-1)//2
		in_k = ((num-1)*(num-2))//2
		dd[key]=use_all - in_k
		total+=use_all
	
	for v in al:
		pp=total-dd[v]
		print(pp)
		
	
	
	
	
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