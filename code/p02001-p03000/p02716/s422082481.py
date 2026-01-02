import sys

input_methods=['clipboard','file','key']
using_method=1
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
mod=1000000007

#+++++

def main():
	n = int(input())
	al = list(IN())
	if n == 2 or n == 3:
		return max(al)
	
	if n % 2 == 0:
		cc = [[0]*n,[0]*n]
		cc[0][0]=al[0]
		cc[1][1]=al[1]
		for i in range(2,n):
			if i%2==0:
				cc[0][i]=cc[0][i-2]+al[i]
			else:
				cc[1][i]=max(cc[1][i-2],cc[0][i-3])+al[i]
		return max(cc[0][-2], cc[1][-1])
		
	else:
		cc = [[0]*n,[0]*n, [0]*n]
		cc[0][0]=al[0]
		cc[1][1]=al[1]
		cc[0][2]=al[2]+al[0]
		cc[2][2]=al[2]
		for i in range(3, n):
			if i % 2 ==1:
				cc[1][i]=max(cc[1][i-2],cc[0][i-3])+al[i]
			else:
				cc[0][i]=cc[0][i-2]+al[i]
				cc[2][i]=max(cc[0][i-4],cc[1][i-3],cc[2][i-2])+al[i]
		return max(cc[0][-3],cc[1][-2],cc[2][-1])
				
	
		
	
	
	
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