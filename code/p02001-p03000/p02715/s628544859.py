import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
mod=1000000007

#+++++

def main():
	#a = int(input())
	k, n = IN()
	#s = input()
	bb=[0]*n
	for i in range(n,0,-1):
		pattern = pow((n//i), k, mod)
		for b in range(2, n+1):
			if (i * b)-1 >= n:
				break
			pattern -= bb[(i*b)-1]
			pattern %= mod
		bb[i-1]=pattern
	ret=0
	#print(bb)
	for i, v in enumerate(bb):
		ret += v*(i+1)
		ret %=mod
	return ret
		
		
		
	
	
	ret=pow(b,c,mod)
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