import sys

input_methods=['clipboard','file','key']
using_method=2
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
mod=1000000007

#+++++

def is_gg(s):
	if len(s)%2 == 1:
		return False
		
	mannaka=len(s)//2
	for a,b in zip(s, s[mannaka:]):
		if a!=b:
			return False
	return True
	
	
def main():
	s = input()
	for i in range(1, len(s)):
		if is_gg(s[:len(s)-i]):
			return len(s) - i
	
	
	
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