import sys
import queue
import bisect

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
mod=1000000007

#+++++

def main_b1():
	n, a, b = IN()
	al = [int(input()) for _ in range(n)]
	if len(al)==1:
		return (al[0] + a -1)//a
	
	al.sort()
	max_value = al[-1]
	min_value = al[0]
	dd_queue = queue.PriorityQueue()
	for v in al:
		dd_queue.put((-v, v))
		
	cc=0
	dmage_diff = a-b
	while True:
		_, max_hp=dd_queue.get()
		if max_hp-(b*cc) <= 0:
			return cc
			
		_, second_max_hp = dd_queue.get()
		nb = ((max_hp-second_max_hp)+dmage_diff-1)//dmage_diff
		
		if max_hp <= nb * a:
			return (max_hp + a - 1)//a
		
		cc += nb
		next_hp=max_hp-dmage_diff*nb
		dd_queue.put((-next_hp, next_hp))
		dd_queue.put((-second_max_hp, second_max_hp))

def is_ok(sorted_list, c, a, b):
	ii=bisect.bisect_right(sorted_list,b*c)
	count=c
	diff=a-b
	for v in sorted_list[ii:]:
		nokori = v - c*b
		count -= (nokori+diff-1)//diff
		if count < 0:
			return False
	return True

def main():
	n, a, b = IN()
	al = [int(input()) for _ in range(n)]
	al.sort()
	
	ok = (al[-1]+b-1)//b
	ng = 0
	while ok-ng > 1:
		mm=(ok+ng)//2
		if is_ok(al, mm, a, b):
			ok = mm
		else:
			ng = mm
	return ok
		
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