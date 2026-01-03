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
	#a = int(input())
	v = [-1]*1001
	v[0]=0
	v[1]=0
	for i in range(2,1000+1):
		if v[i] == -1:
			c=1
			while c * i <= 1000:
				v[c*i] = i
				c+= 1
	
	n = int(input())
	dd=collections.defaultdict(lambda :0)
	for i in range(2, n+1):
		p=i
		while p > 1:
			yakusuu = v[p]
			dd[yakusuu] += 1
			p = p // yakusuu
	
	ret = 1
	for k in dd:
		ret *= dd[k]+1
		ret %= mod
		
	return ret
	
	
	#b , c = tin()
	#s = input()	
	
	
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