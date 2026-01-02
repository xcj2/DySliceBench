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
	a = int(input())
	#b , c = tin()
	#s = input()
	dd = defaultdict(lambda :0)
	for i in range(2, a):
		while a % i == 0:
			dd[i]+=1
			a = a // i
		if i ** 2 > a:
			if a != 1:
				dd[a]+=1
			break
	
	ret = 0
	for key in dd:
		v = dd[key]
		for i in range(1, 100):
			if v < i:
				break
			v -= i
			ret += 1
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