import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def dd(b, n, k):
	if k==0:
		return n
	if b <= k:
		return 0
	ret = 0
	na = n // b
	ret += na * (b-k)
	
	nb = n % b
	ret += max(nb - k + 1, 0)
	#pa((b,ret))
	return ret

def main():
	#a = int(input())
	n, k = tin()
	#s = input()
	ret = 0
	for b in range(1, n+1):
		ret += dd(b,n, k)
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