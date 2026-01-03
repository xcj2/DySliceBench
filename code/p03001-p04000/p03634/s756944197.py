import sys
import queue

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def main():
	n = int(input())
	graph = [[] for _ in range(n)]
	for _ in range(n-1):
		a, b, d = tin()
		graph[a-1].append((b-1, d))
		graph[b-1].append((a-1, d))
	#s = input()
	q, k = tin()
	dist = [-1]*n
	dist[k-1] = 0
	qu=queue.Queue()
	qu.put(k-1)
	while not qu.empty():
		pos = qu.get()
		for v, d in graph[pos]:
			if dist[v] == -1:
				dist[v] = dist[pos] + d
				qu.put(v)
	
	for _ in range(q):
		f, t = tin()
		print(dist[f-1] + dist[t-1])
	
	
	
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