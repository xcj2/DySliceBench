import sys
import collections

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=998244353
 

#+++++

def main():
	n = int(input())
	#b , c = tin()
	#s = input()
	al = lin()
	if al[0] != 0:
		return 0
	if al.count(0) != 1:
		return 0
	
	alc = collections.Counter(al)
	mm = max(alc.keys())
	
	b = alc.keys()
	b=list(b)
	b.sort()
	if list(range(mm+1)) != b:
		#pa('rrrr')
		return 0
		
	v = 1
	p=1
	for k in range(1, mm+1):
		num = alc[k]
		add = pow(p, num, mod)
		v *= add
		v %= mod
		p = num
	return v
		
	
	
	
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