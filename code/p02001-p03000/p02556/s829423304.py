import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def main():
	n = int(input())
	#b , c = tin()
	#s = input()	
	pp_min=mod*mod
	pp_max=0
	pm_max=-mod*mod
	mp_max=-mod*mod
	for _ in range(n):
		a, b = tin()
		pp_min = min(pp_min, a+b)
		pp_max = max(pp_max, a+b)
		pm_max = max(pm_max, a-b)
		mp_max = max(mp_max, -a + b)
	return max((pp_max - pp_min), (mp_max + pm_max))
	
	
	
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