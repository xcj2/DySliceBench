import sys
import queue
import collections

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def ccc(start, goal, mat):
	open=queue.PriorityQueue()
	close=set()
	open.put((0, start))
	
	while True:
		cost, pos = open.get()
		#pa((cost,pos))
		if pos == 1:
			return cost
		if pos in close:
			continue
		for i in range(0,9+1):
			if i == pos:
				continue
			open.put((cost + mat[pos][i], i))
		else:
			close.add(pos)
	
	return -1

def main():
	#a = int(input())
	h, w = tin()
	#s = input()
	mm = [lin() for _ in range(10)]
	dist=dict()
	for i in range(0, 9+1):
		dist[i] = ccc(i,1,mm)
	dist[-1]=0
	
	ret=0
	for hi in range(h):
		al = lin()
		for v in al:
			ret += dist[v]
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