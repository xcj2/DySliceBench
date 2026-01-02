import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def main():
	n = int(input())
	#b , c = tin()
	#s = input()
	al = lin()
	lzero = [0]*62
	lone = [0]*62
	for v in al:
		for i in range(62):
			if v & (2**i) > 0:
				lone[i] += 1
			else:
				lzero[i] += 1
	ret = 0
	for i, (n_one, n_zero) in enumerate(zip(lone, lzero)):
		t = pow(2, i, mod) * n_one * n_zero
		ret += t
		ret %= mod
		
	print(ret)
		
			
	
	
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