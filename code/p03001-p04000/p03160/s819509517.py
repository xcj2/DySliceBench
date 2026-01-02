import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
LIN=lambda : list(IN())
mod=1000000007

#+++++

def main():
	n = int(input())
	#b , c = IN()
	#s = input()
	al = LIN()
	c = 0
	nc = mod
	nnc = mod
	for cv, nv, nnv in zip(al, al[1:], al[2:]):
		nc = min(c + abs(cv - nv), nc)
		nnc = min(nnc, c+ abs(cv - nnv))
		c, nc, nnc = nc, nnc, mod
	nc = min(c + abs(al[-2] - al[-1]), nc)
	c = nc
	
	print(c)
	
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