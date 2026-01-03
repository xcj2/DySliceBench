import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
LIN=lambda : list(IN())
mod=1000000007

#+++++

def main():
	#a = int(input())
	n , l = IN()
	#s = input()
	al = LIN()
	for i in range(len(al)-1):
		if al[i]+al[i+1] >= l:
			break
	else:
		print('Impossible')
		return 
	print('Possible')
	last_tie = i + 1
	pa(('lt',last_tie))
	for i in range(1, last_tie):
		print(i)
	for i in range(n-1, last_tie, -1):
		print(i)
	print(last_tie)
	
	
	
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