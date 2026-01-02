import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def main():
	#n = int(input())
	#b , c = tin()
	#s = input()
	s=input()
	pre='C'
	ret = 0
	a_num=0
	for c in s:
		d = pre + c
		if d == 'AA':
			a_num += 1
		elif d == 'BA':
			a_num=1
		elif d == 'CA':
			a_num += 1
		elif d == 'AB':
			pass
		elif d== 'BB':
			a_num = 0
		elif d == 'CB':
			pass
		elif d == 'AC':
			a_num = 0
		elif d == 'BC':
			ret += a_num
		else:
			a_num = 0
		
		pre = c
	return ret
	
	
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