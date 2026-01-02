import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
mod=1000000007

#+++++

def main():
	#a = int(input())
	n, k = IN()
	#s = input()
	kk=0
	for i in range(k-1):
		kk += i
		kk %= mod
		
	bb=0
	for i in range(k-1):
		bb += (n )- i
		bb %= mod
	cc=0
	#cc += (bb - kk)%mod
	#pa((bb,kk,cc))
	for i in range(k, n+2):
		bb += (n + 1) - i
		bb %= mod
		kk += i-1
		kk %= mod
		cc += (bb - kk + 1)
		cc%= mod 
		#pa((bb,kk,cc))
	print(cc)
	
	
	
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