import sys
import collections

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
	al=lin()
	cc=collections.defaultdict(lambda :0)
	for v in al:
		cc[v]+=1
	num2=0
	num1=0
	for k in cc:
		if cc[k]> 1 and cc[k]%2==1:
			cc[k]=1
			num1+=1
		elif cc[k]>1:
			cc[k]=2
			num2+=1
		else:
			num1+=1
	ret=num1
	if num2 % 2 == 1:
		ret += num2 - 1
	else:
		ret += num2
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