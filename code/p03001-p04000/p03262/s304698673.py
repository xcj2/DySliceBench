import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
mod=1000000007

#+++++

def ggg(a,b):
	while b>0:
		nb=a%b
		na=b
		a,b=na,nb
	return a
		

def main():
	n, x = IN()
	al = list(IN())
	al.append(x)
	al.sort()
	bl=[b-a for a,b in zip(al,al[1:])]
	ret=bl[0]
	for diff in bl:
		ret = ggg(ret, diff)
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