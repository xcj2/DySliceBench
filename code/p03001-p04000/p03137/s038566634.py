import sys

input_methods=['clipboard','file','key']
using_method=1
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def main():
	#a = int(input())
	n, m = tin()
	al = lin()
	#s = input()
	al.sort()
	diff_al = [abs(vj-vi) for vi, vj in zip(al, al[1:])]
	#pa(al)
	#pa(diff_al)
	diff_al.sort()
	#pa(diff_al)
	if n == 1:
		ret = sum(diff_al)
	else:
		ret = sum(diff_al[:-(n-1)])
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