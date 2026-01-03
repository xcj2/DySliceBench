import sys

input_methods=['clipboard','file','key']
using_method=1
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
mod=1000000007

#+++++

def icc(c):
	ret=(ord('z') - ord(c) + 1)
	return ret
	
def nn(c,v):
	ret=chr(ord(c)+v)
	return ret

def main():
	s=input()
	n = int(input())
	#b , c = IN()
	#s = input()
	ret = []
	for c in s:
		#print(c,icc(c),n)
		if c != 'a' and icc(c) <= n:
			ret.append('a')
			n-=icc(c)
		else:
			ret.append(c)
	
	n%=26
	if icc(ret[-1]) <= n:
		n-=icc(ret[-1])
		ret[-1]='a'
	ret[-1]=nn(ret[-1], n)
	#pa(ret)
	return ''.join(ret)
	
	
	
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