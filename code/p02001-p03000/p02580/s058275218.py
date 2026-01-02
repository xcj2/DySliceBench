import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def main():
	#a = int(input())
	h, w, m = tin()
	#s = input()
	hl=[0]*h
	wl=[0]*w
	is_on=set()
	for _ in range(m):
		hi,wi=tin()
		hl[hi-1]+=1
		wl[wi-1]+=1
		is_on.add(hi*mod+wi)
	max_h=max(hl)
	max_w=max(wl)
	t_return = max(hl)+max(wl)
	max_ids_hl=[i+1 for i,v in enumerate(hl) if v == max_h]
	max_ids_wl=[i+1 for i,v in enumerate(wl) if v == max_w]
	if len(max_ids_hl)*len(max_ids_wl) > len(is_on):
		return t_return
	for hi in max_ids_hl:
		for wi in max_ids_wl:
			if hi*mod + wi not in is_on:
				return t_return
	return t_return-1
	
	
		
		
	
	
	
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