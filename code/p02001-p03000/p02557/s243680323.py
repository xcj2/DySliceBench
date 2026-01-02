import sys
import collections
import queue

input_methods=['clipboard','file','key']
using_method=1
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def main():
	n = int(input())
	#b , c = tin()
	#s = input()	
	al = lin()
	bl = lin()
	al_c = collections.Counter(al)
	bl_c = collections.Counter(bl)
	ooo=queue.PriorityQueue()
	for k in al_c:
		if k not in bl_c:
			continue
			
		tt = al_c[k]+bl_c[k]
		if tt > n:
			print('No')
			return
		ooo.put((-tt, k))
		
	for k in bl_c:
		if k not in al_c:
			ooo.put((mod-k, k))
	
	print('Yes')
	ret = olt2(n,al,bl)
	print(*ret)
	return 
	
	ret = [-1] * n
	yobi = None
	_, cc = ooo.get()
	(_, yobi) = (_, None) if ooo.empty() else ooo.get()
	for i, v in enumerate(al):
		#pa((i,v,cc,yobi))
		if bl_c[cc] == 0:
			cc = yobi
			nn, yobi = (_, None) if ooo.empty() else ooo.get()
			while yobi is not None and nn< 0 and yobi < v:
				ooo.put((mod - yobi, yobi))
				nn, yobi = (_, None) if ooo.empty() else ooo.get()
		
		if cc == v and yobi is None and ooo.empty():
			rr = olt2(n, al, bl)
			if rr is not None:
				print(*ret)
			return None
		
		if cc != v:
			ret[i] = cc
			bl_c[cc] -= 1
		else:
			ret[i] = yobi
			bl_c[yobi] -= 1
			if bl_c[yobi]==0:
				#pa('yyy')
				nn, yobi = (_, None) if ooo.empty() else ooo.get()
				while yobi is not None and nn < 0 and yobi < v:
					ooo.put((mod - yobi, yobi))
					nn, yobi = (_, None) if ooo.empty() else ooo.get()
			
	print(*ret)
			
			
def olt(n, al, bl):
	al_c = collections.Counter(al)
	bl_c = collections.Counter(bl)
	ooo=queue.PriorityQueue()
	for k in al_c:
		if k not in bl_c:
			continue
			
		tt = al_c[k]+bl_c[k]
		if tt > n:
			print('No')
			return
		ooo.put((-bl_c[k], k))
		
	for k in bl_c:
		if k not in al_c:
			ooo.put((mod-k, k))
	
	ret = [-1] * n
	yobi = None
	_, cc = ooo.get()
	(_, yobi) = (_, None) if ooo.empty() else ooo.get()
	for i, v in enumerate(al):
		#pa((i,v,cc,yobi))
		if bl_c[cc] == 0:
			cc = yobi
			nn, yobi = (_, None) if ooo.empty() else ooo.get()
			while yobi is not None and nn< 0 and yobi < v:
				ooo.put((mod - yobi, yobi))
				nn, yobi = (_, None) if ooo.empty() else ooo.get()
		
		if cc == v and yobi is None and ooo.empty():
			ret = olt2(n, al, bl)
			print(*ret)
			return
		
		if cc != v:
			ret[i] = cc
			bl_c[cc] -= 1
		else:
			ret[i] = yobi
			bl_c[yobi] -= 1
			if bl_c[yobi]==0:
				#pa('yyy')
				nn, yobi = (_, None) if ooo.empty() else ooo.get()
				while yobi is not None and nn < 0 and yobi < v:
					ooo.put((mod - yobi, yobi))
					nn, yobi = (_, None) if ooo.empty() else ooo.get()
	print(*ret)
	return None
	

def olt2(n, al, bl):
	al_c = collections.Counter(al)
	bl_c = collections.Counter(bl)
	ooo=queue.PriorityQueue()
	for k in al_c:
		if k not in bl_c:
			continue
			
		tt = al_c[k]+bl_c[k]
		ooo.put((-tt, k))
		
	for k in bl_c:
		if k not in al_c:
			ooo.put((mod-k, k))
	
	ret = [-1] * n
	cv, cc = ooo.get()
	hold = None
	for i, v in enumerate(al):
		#pa((i,v,cc,cv))
		if cc == v and ooo.empty():
			return 1/0
		elif cc == v:
			ooo.put((mod+mod+cc, cc))
			cv, cc = ooo.get()
		
		while (cc < v and cv < 0) or cc == v:
			ooo.put((mod+cc+(0 if cc != v else mod), cc))
			pre = cv,cc
			cv, cc = ooo.get()
			if pre == (cv, cc):
				return 1/0
				
		ret[i]=cc
		bl_c[cc] -= 1
		if bl_c[cc] <= 0:
			cv, cc = (0,-1) if ooo.empty() else ooo.get()
			
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