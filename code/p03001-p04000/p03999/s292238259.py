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
	ret=0
	for i in range(len(s)):
		for j in range(i, len(s)):
			#print(i,len(s)-j-1,s[i:j+1])
			v = int(s[i:j+1])
			if i >= 1:
				na =2 ** (i-1)
			else:
				na=1
			
			if len(s)-j-1 >= 1:
				nb= 2**(len(s)-j-2)
			else:
				nb=1
			ret += v*na*nb
			#print(na,nb)
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