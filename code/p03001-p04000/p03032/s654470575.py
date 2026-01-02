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
	n, k = IN()
	dq = LIN()
	rdq = dq[::-1]
	#s = input()
	max_v=0
	for left_get in range(k+1):
		for right_get in range(max(k-left_get+1,1)):
			if left_get+right_get>n:
				continue
			elif left_get==0 and right_get==0:
				continue
			nokori=k-left_get-right_get
			l=dq[:left_get]
			r=rdq[:right_get]
			#print(l, r)
			dd=(l+r)
			dd.sort(reverse=True)
			for _ in range(nokori):
				if dd[-1]>= 0:
					break
				dd.pop()
				if len(dd)==0:
					break
			r=sum(dd)
			max_v=max(max_v, r)
	print(max_v)
		
		
	
	
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