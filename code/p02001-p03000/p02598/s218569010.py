import sys
import math

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def cc(al, v_max, k):
	for vl in al:
		if vl <= v_max:
			return True
		k -= ((vl + v_max- 1) // v_max) - 1
		#pa((k, -(-v // v_max)))
		if k < 0:
			return False
	return True
		

def main():
	#a = int(input())
	n, k = tin()
	#s = input()
	al = lin()
	al.sort(reverse = True)
	#print(al)
	ok = al[0]
	ng = 0
	while ok - ng > 1:
		mid = (ok + ng)//2
		ii=cc(al, mid, k)
		#pa((mid,ii))
		if ii:
			ok = mid
		else:
			ng = mid
	#pa(ok)
	print(ok)
	
	
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