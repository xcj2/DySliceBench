import sys
import collections

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
	al = lin()
	al.sort()
	
	unique_al = list(set(al))
	unique_al.sort()
	
	al_counter = collections.Counter(al)
	ok=[v for v in al_counter.keys() if al_counter[v] == 1]
	d = {v:i for i,v in enumerate(ok)}
	max_v = 10**6+1
	for check in unique_al:
		for v in range(2*check, max_v, check):
			if v in d:
				ok[d[v]]=0
				
	return sum([v > 0 for v in ok ])
		
	
	
	
	
	
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