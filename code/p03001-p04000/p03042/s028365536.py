import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
mod=1000000007

#+++++

#https://atcoder.jp/contests/abc126/tasks/abc126_b

def is_mm(s):
	return int(s) >= 1 and int(s) <= 12

def is_yy(s):
	return True

def main():
	#a = int(input())
	#b , c = IN()
	s = input()
	is_mmxx=is_mm(s[:2])
	is_yyxx=is_yy(s[:2])
	is_xxmm=is_mm(s[2:])
	is_xxyy=is_yy(s[2:])
	ra = 'AMBIGUOUS'
	rb = 'NA'
	rc = 'YYMM'
	rd = 'MMYY'
	
	if is_mmxx and is_xxyy and is_xxmm and is_yyxx:
		return ra
	elif is_mmxx and is_xxyy:
		return rd
	elif is_yyxx and is_xxmm:
		return rc
	else:
		return rb
	
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