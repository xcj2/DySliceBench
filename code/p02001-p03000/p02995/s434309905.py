import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
mod=1000000007

#+++++

def ppp(c,d):
	while c % d != 0:
		nc = d
		nd = c % d
		c,d = nc, nd
	return d

def main():
	a, b, c, d = IN()
	cad=(c*d)//ppp(c,d)
	
	
	all_num=b-a+1
	can_c=(b//c) - ((a-1)//c)
	can_d = (b//d) - ((a-1)//d)
	can_c_and_d = (b//(cad)) - ((a-1)//(cad))
	ret = all_num-can_c-can_d+can_c_and_d
	#pa((can_c,can_d,can_c_and_d,all_num))
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