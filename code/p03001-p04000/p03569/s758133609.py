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
	#b , c = tin()
	s = list(input())
	cc=[c for c in s if c != 'x']
	ccc=cc[::-1]
	if cc != ccc:
		return -1
	add=0
	ci=0
	ls = len(s)
	for i, c in enumerate(s):
		#cc = s[ls-1-ci]
		#if cc == c:
		#	ci+=1
		#else:
		while c != s[ls-1-ci]:
			pa((i,ci,c,s[ls-1-ci]))
			if c == 'x':
				add+=1
				ci-=1
				break
			else:
				add+=1
				ci+=1
		ci+=1
		if i + ci >= ls:
			break
	return add
	
	
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