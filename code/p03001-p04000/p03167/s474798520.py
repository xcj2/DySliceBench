import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
LIN=lambda : list(IN())
mod=1000000007

#+++++

def main():
	#a = int(input())
	h, w = IN()
	#s = input()
	map_l = [input() for _ in range(h)]
	l_l = [[0] * w for _ in range(h)]
	l_l[0][0]=1
	for hi in range(h):
		for wi in range(w):
			if map_l[hi][wi] == '#':
				continue
			if wi > 0:
				l_l[hi][wi] += l_l[hi][wi-1]
				l_l[hi][wi] %= mod
			if hi > 0:
				l_l[hi][wi] += l_l[hi-1][wi]
				l_l[hi][wi] %= mod
				
	print(l_l[h-1][w-1])
		
	
	
	
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