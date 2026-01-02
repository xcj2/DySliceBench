import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def main():
	#a = int(input())
	n, k, c_yutori = tin()
	if n == 1:
		return 1
		
		
	s = input()
	can_work = [0]*n
	can_work[0] = 1 if s[0]=='o' else 0
	yn = c_yutori if s[0]=='o' else 0
	for i, c in enumerate( list(s)[1:],1):
		if yn == 0 and c == 'o':
			can_work[i] = can_work[i-1]+1
			yn = c_yutori
		else:
			can_work[i] = can_work[i-1]
			yn = max(0, yn - 1)
	need_to_work = [k]*n
	if s[-1]=='o':
		need_to_work[-1] = k-1
		yn = c_yutori
	else:
		need_to_work[-1]=k
		yn=0
	for i, c in enumerate(list(s)[-2::-1],1):
		pos = n-i-1
		if yn == 0 and c == 'o':
			need_to_work[pos] = need_to_work[pos+1]-1
			yn = c_yutori
		else:
			need_to_work[pos]=need_to_work[pos+1]
			yn = max(0, yn-1)
	#pa(can_work)
	#pa(need_to_work)
	if need_to_work[1] == 1:
		print(1)
		
	for i in range(1, n-1):
		if can_work[i-1] < need_to_work[i+1]:
			print(i+1)
		
	if can_work[-2]==k-1:
		print(n)
		
		
		
			
		
	
	
	
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