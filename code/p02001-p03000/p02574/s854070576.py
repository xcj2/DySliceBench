import sys
import math

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def gcd(a, b):
	return math.gcd(a, b)
	
def is_pc(al):
	mm=((10**6)+5)
	dd = [0]* mm
	kk = [-1]* mm
	
	for v in al:
		dd[v] += 1
	
	for i, _ in enumerate(kk):
		if i <= 1:
			continue
		if kk[i]==-1:
			n=1
			nd = 0
			while i*n < mm:
				kk[i*n]=1
				nd += dd[i*n]
				n+=1
		if nd >= 2:
			return False
	return True

def main():
	n = int(input())
	#b , c = tin()
	#s = input()	
	al = lin()
	
	pc = 'pairwise coprime'
	sc = 'setwise coprime'
	nc = 'not coprime'
	if is_pc(al):
		return pc
	v=al[0]
	for vv in al:
		v = gcd(v, vv)
	if v == 1:
		return sc
	return nc
	
				
		
	
	
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