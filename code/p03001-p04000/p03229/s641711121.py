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
	al = [int(input()) for _ in range(n)]
	al.sort()
	l = 1
	r = n-1
	ret = 0
	stl=al[0]
	str=al[0]
	while l <= r:
		g = [abs(stl - al[l]), abs(stl-al[r]), abs(str - al[l]), abs(str - al[r])]
		if max(g) == g[0] or max(g) == g[2]:
			up = al[l]
			l+=1
		else:
			up = al[r]
			r -= 1
			
		if max(g) == g[0]:
			stl = up
		elif max(g)==g[2]:
			str = up
		elif max(g)==g[1]:
			stl=up
		else:
			str = up
		ret +=max(g)
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