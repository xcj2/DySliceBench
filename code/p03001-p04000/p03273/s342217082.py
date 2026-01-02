import sys
import numpy as np

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def kk(al):
	for i in range(len(al)-1, -1, -1):
		if list(al[i]) == ['.']*len(al[i]):
			al = np.delete(al, i, 0)
	return al

def main():
	#a = int(input())
	h, w = tin()
	#s = input()
	al=[]
	for _ in range(h):
		s=list(input())
		al.append(s)
	al = np.array(al)
	al = kk(al)
	al = kk(al.T)
	al=al.T
	for v in al:
		print(''.join(v))
		
	
	
	
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