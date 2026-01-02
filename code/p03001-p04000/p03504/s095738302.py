import sys
import queue

input_methods=['clipboard','file','key']
using_method=1
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def ddd(al, c):
	rcq = queue.PriorityQueue()
	for _ in range(c):
		rcq.put(0)
	for st, ed in al:
		earliest = rcq.get()
		#pa((earliest,st))
		if earliest >= st-0.5:
			return False
		rcq.put(ed)
	return True

def main():
	#a = int(input())
	n, c = tin()
	#s = input()
	dd=[[] for _ in range(c)]
	for _ in range(n):
		s, t, cv = tin()
		dd[cv-1].append((s,t))
	#for cl in dd:
	#	pa(cl)
	
	aal=[]
	for cl in dd:
		if len(cl)==0:
			continue
		cl.sort()
		sa, ta = cl[0]
		for s, t in cl[1:]:
			if ta == s:
				ta = t
			else:
				aal.append((sa, ta))
				sa,ta = s, t
		else:
			aal.append((sa, ta))
			
	#aal = [list(tin()) for _ in range(n)]
	aal.sort()
	#pa(aal)
	for i in range(1, c+1):
		is_ok = ddd(aal, i)
		#pa(i)
		if is_ok:
			return i
	
	
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