import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def main():
	#a = int(input())
	#b , c = tin()
	#s = input()
	vl = [lin() for _ in range(3)]
	for f, t in [(0,1), (1,2), (2,0)]:
		is_same = set()
		for i in range(3):
			is_same.add(vl[f][i] - vl[t][i])
		if len(is_same) != 1:
			return 'No'
		
	for f, t in [(0,1), (1,2), (2,0)]:
		is_same = set()
		for i in range(3):
			is_same.add(vl[i][f] - vl[i][t])
		if len(is_same) != 1:
			return 'No'
	return 'Yes'
	
			
	
	
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