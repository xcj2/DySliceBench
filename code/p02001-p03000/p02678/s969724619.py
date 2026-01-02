import sys
import queue

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(IN())
mod=1000000007

#+++++

def main():
	#a = int(input())
	n, m = tin()
	#s = input()
	mm = [[] for _ in range(n)]
	rrp=[-1]*n
	for _ in range(m):
		a,b = tin()
		mm[a-1].append(b-1)
		mm[b-1].append(a-1)
	
	q = queue.Queue()
	q.put((0,0))
	while not q.empty():
		pos, parent = q.get()
		if rrp[pos] >= 0:
			continue
		rrp[pos] = parent
		
		for v in mm[pos]:
			q.put((v, pos))
	print('Yes')
	for v in rrp[1:]:
		print(v+1)
	
	
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