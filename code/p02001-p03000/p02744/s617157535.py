import sys

input_methods=['clipboard','file','key']
using_method=1
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
mod=1000000007

#+++++

global ll
ll=['a','b','c','d','e','f','g','h','i','j']

def mm(sl, i, m):
	if len(sl)==i:
		print(''.join(sl))
		return
	for j in range(m+1):
		sl[i]=ll[j]
		mm(sl, i+1, m)
	sl[i]=ll[m+1]
	mm(sl, i+1, m+1)
	

def main():
	n = int(input())
	sl=['a']*n
	mm(sl, 1, 0)
	
	
	
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