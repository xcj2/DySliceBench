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

def main():
	# = int(input())
	n, m, k = tin()
	#s = input()
	friend_l = [[] for _ in range(n)]
	for _ in range(m):
		a, b = tin()
		a, b = a-1, b-1
		friend_l[a].append(b)
		friend_l[b].append(a)
	
	friend_group=[-1]*n
	gid=1
	st=0
	while st < n:
		if friend_group[st] > 0:
			st += 1
			continue
		friend_group[st] = gid
		qq=queue.Queue()
		qq.put(st)
		while not qq.empty():
			f = qq.get()
			for t in friend_l[f]:
				if friend_group[t] == -1:
					friend_group[t] = gid
					qq.put(t)
		gid += 1
				
	num_mem = collections.Counter(friend_group)
	
	#about block
	bl=[[] for _ in range(n)]
	bln = [0]*n
	for _ in range(k):
		a,b = tin()
		a,b = a-1, b-1
		if friend_group[a] == friend_group[b]:
			bln[a]+=1
			bln[b]+=1
			
	ret=[]
		
	for i in range(n):
		full = num_mem[friend_group[i]]
		fn = len(friend_l[i])
		p=(full-fn-bln[i] -1)
		ret.append(p)
	print(*ret)
	
		
	
	
	
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