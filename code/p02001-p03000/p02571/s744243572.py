import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def kotonaru_num(a, b):
	if len(a) != len(b):
		return 1/0
	ret = 0
	for c, s in zip(a, b):
		if c != s:
			ret += 1
			
	return ret
 

def main():
	#a = int(input())
	#b , c = tin()
	s = input()	
	t = input()
	ret = mod
	for i in range(len(s) - len(t)+1):
		cc = s[i:i+len(t)]
		#pa(cc)
		tr = kotonaru_num(cc, t)
		ret = min(ret, tr)
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