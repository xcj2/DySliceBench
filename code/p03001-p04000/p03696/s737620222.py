import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
mod=1000000007

#+++++

def main():
	n = int(input())
	#b , c = IN()
	s = input()
	rc=0
	rc_max=0
	for c in s:
		if c == ')':
			rc+=1
			rc_max=max(rc_max, rc)
		else:
			rc -= 1
	
	lc=0
	lc_max=0
	for c in s[::-1]:
		if c == '(':
			lc += 1
			lc_max=max(lc, lc_max)
		else:
			lc -= 1
	ret = '(' * rc_max + s + ')'*lc_max
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