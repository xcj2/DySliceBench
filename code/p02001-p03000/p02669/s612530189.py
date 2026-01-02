import sys
import queue

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(IN())
mod=1000000007

#+++++

def ggg(n,a,b,c,d):
	init = n
	open = queue.PriorityQueue()
	close = set()
	open.put((0, n))
	min_v = n*d
	while not open.empty():
		cost, pos = open.get()
		if pos in close:
			continue
		if cost > min_v:
			continue
		
		min_v = min(min_v, cost+pos*d)
		for c, add in zip([a,b,c],[2,3,5]):
			k = pos % add
			nc = cost + k*d + c
			np = pos // add
			if nc <= min_v and np not in close:
				open.put((nc, np))
				#pa((nc,np))
			nnc = cost + (add-k) *d + c
			nnp = (pos + add) // add
			if nnc <= min_v and nnp not in close:
				open.put((nnc, nnp))
				#pa((nnc,nnp))
		close.add(pos)
	return min_v
		
		



def main():
	t = int(input())
	for i in range(t):
		n, a, b , c, d = tin()
		r = ggg(n,a,b,c,d)
		print(r)
	#s = input()
	
	
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