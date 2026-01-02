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
	n , k = IN()
	al = LIN()
	#s = input()
	rr = ['0']*(k+1)
	
	for i in range(k+1):
		if i < al[0]:
			rr[i]='l'
		
		for v in al:
			if v > i:
				pass
			if rr[i-v] == 'l':
				rr[i]='w'
				break
		else:
			rr[i]='l'
	ret = 'First' if rr[-1] == 'w' else 'Second'
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