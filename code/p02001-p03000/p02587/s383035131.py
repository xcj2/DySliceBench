import sys
import queue

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def is_kaibun(s):
	if len(s) <= 1:
		return True
	for c, cc in zip(s,s[::-1]):
		if c != cc:
			return False
	return True
	
	
def mk_sub(s, other, s_is_front):
	#pa((s,other,s[:len(other)],other[:len(s)]))
	if len(s) <= len(other) and s == other[:len(s)]:
		return True, other[len(s):], not s_is_front
	elif len(s)>len(other) and s[:len(other)] == other:
		return True, s[len(other):], s_is_front
	return False, '', False

def main():
	n = int(input())
	#b , c = tin()
	#s = input()
	dd_f = {}
	dd_b = {}
	for _ in range(n):
		s, v = input().split()
		v = int(v)
		if s in dd_f:
			v = min(v, dd_f[s])
		dd_f[s] = v
		dd_b[s[::-1]]=v
	front=True
	open_list=queue.PriorityQueue()
	close_list_f = set()
	close_list_b = set()
	for k in dd_f:
		open_list.put((dd_f[k], (k, front)))
		
	while not open_list.empty():
		#pa('rrrr')
		#return 
		cost, (s, is_front) = open_list.get()
		#pa((cost,s,is_front))
		#pa(s if is_front else s[::-1])
		if is_kaibun(s):
			return cost
		if (is_front and s in close_list_f) or (not is_front and s in close_list_b):
			continue
		if is_front:
			close_list_f.add(s)
		else:
			close_list_b.add(s)
			
		dic = dd_b if is_front else dd_f
		for k in dic:
			is_ok, next_s, r_is_front=mk_sub(s, k, is_front)
			#pa((is_ok,next_s,r_is_front,k))
			if not is_ok:
				continue
			elif r_is_front and next_s in close_list_f:
				continue
			elif not r_is_front and next_s in close_list_b:
				continue
			else:
				open_list.put((cost + dic[k], (next_s, r_is_front)))
		
	return -1
		
	
	
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