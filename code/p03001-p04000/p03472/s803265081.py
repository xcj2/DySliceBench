import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
mod=1000000007

#+++++

def main():
	n , h = IN()
	al=[]
	bl=[]
	for i in range(n):
		a,b=IN()
		al.append(a)
		bl.append(b)
		
	bl.sort(reverse=True)
	al.sort()
	a_max=al[-1]
	
	cc=0
	cc_h=h
	for v in bl:
		if v < a_max:
			break
		cc_h-=v
		cc+=1
		if cc_h<=0:
			return cc
	
	cc+=(cc_h + a_max - 1)//a_max
	return cc	
	
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