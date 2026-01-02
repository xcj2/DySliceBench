import sys
import collections

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def check_path(mp, is_archive, wi, hi):
	w = len(mp[0])
	h = len(mp)
	nb = 0
	nw = 0
	qq=collections.deque()
	st_color = mp[hi][wi]
	nb+=1
	qq.append((wi, hi, st_color))
	is_archive[hi][wi] = 1
	while qq:
		pw, ph, pc = qq.popleft()
		for dw, dh in ((1,0), (-1,0), (0,1),(0,-1)):
			if pw+dw<0 or pw+dw>=w or ph+dh < 0 or ph+dh >= h:
				continue
			if is_archive[ph+dh][pw+dw]>0:
				continue
			if mp[ph+dh][pw+dw]==pc:
				continue
			nc = mp[ph+dh][pw+dw]
			if nc == st_color:
				nb += 1
			else:
				nw += 1
			
			qq.append((pw+dw, ph+dh, nc))
			is_archive[ph+dh][pw+dw]=1
	
	return nb*nw

def main():
	#a = int(input())
	h, w = tin()
	#s = input()
	mp = [input() for _ in range(h)]
	is_archive = [[-1]*w for _ in range(h)]
	ret = 0
	for wi in range(w):
		for hi in range(h):
			if is_archive[hi][wi] != -1:
				continue
			nn = check_path(mp, is_archive, wi, hi)
			ret += nn
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