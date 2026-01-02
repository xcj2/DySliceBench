import sys
import queue
import collections

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=100000000777777

#+++++

def main():
	#a = int(input())
	n, k = tin()
	#s = input()
	al=[lin() for _ in range(n)]
	al.sort(key = lambda x : -x[1])
	use_t = set()
	t_max=collections.defaultdict(lambda :0)
	mm=[]
	ret_ug=0
	for t,v in al[:k]:
		ret_ug += v
		if t in use_t and t_max[t] >= v:
			mm.append(v)
		elif t in use_t:
			mm.append(t_max[t])
			t_max[t]=v
		else:
			t_max[t]=v
			use_t.add(t)
	
	nt=len(use_t)
	ret_ug += nt*nt
	
	nokori = collections.defaultdict(lambda :0)
	for t, v in al[k:]:
		if t in use_t:
			continue
		nokori[t]=max(nokori[t], v)
	upp=[]
	for k in nokori:
		upp.append(nokori[k])
	upp.sort(reverse = True)
	mm.sort()
	ret=ret_ug
	for up_v, mm_v in zip(upp, mm):
		ret_ug += up_v
		ret_ug -= mm_v
		ret_ug += 2*nt + 1
		nt += 1
		ret = max(ret, ret_ug)
		
	print(ret)
		
		
	
		
		
		
		
		
	
	
	
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