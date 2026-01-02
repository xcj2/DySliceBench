import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

results = [-1]*2001
results[0]=0
results[1]=0
results[2]=0

def cc(v):
	global results
	if results[v] >= 0:
		return results[v]
		
	ret = 1
	for i in range(3, v+1):
		ret += cc(v-i)
		ret %= mod
	
	results[v]=ret
	return ret
		
def main():
	s = int(input())
	#b , c = tin()
	#s = input()
	return cc(s)
	
	
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