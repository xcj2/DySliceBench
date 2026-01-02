import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(IN())
mod=1000000007

#+++++

def main():
	#a = int(input())
	#b , c = tin()
	s = input()
	q = int(input())
	ff = []
	bb = []
	frip = False
	for _ in range(q):
		ss = input()
		if ss[0] == '1':
			frip = not frip
		else:
			_a, f, c = ss.split()
			is_ff = ((1 if frip else 0) + (1 if f == '1' else 0 )) % 2 == 1
			if is_ff:
				ff.append(c)
			else:
				bb.append(c)
	
	ret = ''.join(ff[::-1]) + s + ''.join(bb)
	if frip:
		ret = ret[::-1]
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