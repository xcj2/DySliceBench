import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def nn(v, min_v, max_v):
	min_n = (min_v + v - 1) // v
	max_n = max_v // v
	#pa((min_n, max_n))
	if max_n < min_n:
		return -1, -1
	return v * min_n, v * max_n + v - 1

def main():
	n = int(input())
	#b , c = tin()
	#s = input()
	al = lin()
	al = al[::-1]
	min_v, max_v = 2, 2
	for v in al:
		min_v, max_v = nn(v, min_v, max_v)
		if min_v == -1:
			return -1
	print(min_v, max_v)
	
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