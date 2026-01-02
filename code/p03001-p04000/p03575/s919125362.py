import sys
import collections

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def is_bridge(n, pi, to_info):
	is_a=[-1]*n
	q =collections.deque()
	q.append(0)
	#ex = [p[0]-1, p[1] - 1]
	while q:
		pos = q.popleft()
		for to in to_info[pos]:
			if pos in pi and to in pi:
				continue
			if is_a[to] != -1:
				continue
			is_a[to]=1
			q.append(to)
	
	return min(is_a) == -1


def main():
	#a = int(input())
	n, m = tin()
	#s = input()
	path = []
	to_info = [[] for _ in range(n)]
	for _ in range(m):
		a, b = tin()
		path.append([a-1, b-1])
		to_info[a-1].append(b-1)
		to_info[b-1].append(a-1)
		
	ret = 0
	#pa(path)
	for pi in path:
		if is_bridge(n, pi, to_info):
			#pa(pi)
			ret += 1
	print(ret)
	
	
#+++++
isTest=False

def pa(*vl):
	if not isTest:
		return
	for v in vl:
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