import sys

input_methods=['clipboard','file','key']
using_method=1
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(IN())
mod=1000000007

#+++++

def main():
	#a = int(input())
	#b , c = tin()
	s = list(input())[:-1]

	count_s = 0
	delete_num=0
	for c in s:
		if c == 'S':
			count_s+=1
		else: #if c == 'T':
			if count_s == 0:
				pass
			else:
				count_s-=1
				delete_num+=2
	return len(s)-delete_num
	
	
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
		input = sys.stdin.readline
			
	ret = main()
	if ret is not None:
		print(ret)