import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
LIN=lambda : list(IN())
mod=1000000007
inf = 10**12
#+++++

def main():
	#a = int(input())
	n, max_w = IN()
	#s = input()
	dp_v = [inf] * (10**5 + 100)
	dp_v[0] = 0
	for _ in range(n):
		add_v = []
		w, v = IN()
		for i, cv in enumerate(dp_v):
			if dp_v[i] == inf:
				continue
			if dp_v[i] + w < dp_v[i+v]:
				add_v.append((i+v, dp_v[i] + w))
		for i, nv in add_v:
			dp_v[i] = nv
			
	for i, min_w in enumerate(dp_v[::-1]):
		if min_w <= max_w:
			v=len(dp_v)-i-1
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