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
	#s = input()
	if n <= 9:
		return 0
	
	counter = collections.defaultdict(lambda :0)
	for i in range(2,n+1):
		v=i
		for ww in range(2,100):
			if v < ww:
				break
			while v%ww==0:
				counter[ww]+=1
				v=v//ww
				
	#for k in counter:
	#	print(k,counter[k])
	
	ret = 0
	#a**74
	for k in counter:
		if counter[k] >= 74:
			ret += 1
	
	#a**24 * b** 2
	n24 = 0
	n2 = 0
	for k in counter:
		if counter[k] >= 24:
			n24 += 1
		elif counter[k] >= 2:
			n2 += 1
	ret += (n24 * (n24-1))
	ret += n24 * n2
		
	#a**14 * b**4
	n14 = 0
	n4 = 0
	for k in counter:
		if counter[k] >= 14:
			n14 += 1
		elif counter[k] >= 4:
			n4 += 1
	ret += (n14 * (n14-1))
	ret += n14 * n4
	
	#a**4 * b**4 * c**2
	n4 = 0
	n2 = 0
	for k in counter:
		if counter[k] >= 4:
			n4 += 1
		elif counter[k] >= 2:
			n2 += 1
	ret += (n4 * (n4-1) * (n4 - 2)) // 2
	ret += ((n4 * (n4-1)) // 2 ) * n2
	
	return ret
	
	
	
	
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