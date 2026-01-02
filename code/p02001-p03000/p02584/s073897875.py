import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def main():
	#a = int(input())
	x, k, d = tin()
	#s = input()
	na = abs(x) // d
	#pa(na)
	if na >= k:
		return min(abs(x - d*k), abs(x+d*k))
	else:
		xa = x - d*na if x >= 0 else x+d*na
		ka = k-na
		kb = ka%2
		#pa(xa)
		if kb==1:
			return min(abs(xa+d), abs(xa-d))
		else:
			return min(abs(xa-2*d),abs(xa+2*d),abs(xa))
		
	
	
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