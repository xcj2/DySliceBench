import sys
from collections import deque

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
mod=1000000007

#+++++

def main():
	n, x, y = IN()
	al=[]
	for i in range(n):
		ll=[0]*n
		for j in range(n-i):
			ll[i+j]=j
		for j in range(i+1):
			ll[i-j]=j
		
		df = x-1
		dt = y-1
		if ll[y-1] < ll[x-1]:
			df, dt = dt, df
		if ll[dt] < ll[df]+1:
			al.append(ll)
			continue
		ll[dt] = ll[df]+1
		for i in range(dt+1,n):
			if ll[i] < ll[i-1]+1:
				break
			ll[i]=ll[i-1]+1
		for i in range(dt-1,0,-1):
			if ll[i] < ll[i+1]+1:
				break
			ll[i]=ll[i+1]+1
		al.append(ll)
		
	#for l in al:
	#	print(l)
			
	rr=[0]*n
	for i in range(n):
		for j in range(i+1,n):
			rr[ al[i][j] ]+=1
	
	for v in rr[1:]:
		print(v)

def main2():
	n, x, y = IN()
	al=[[-1]*n for _ in range(n)]
	ol=queue.Queue()
	for i in range(n):
		al[i][i]=0
	
	for i in range(n-1):
		al[i][i+1]=1
		ol.put((i,i+1))
		al[i+1][i]=1
	al[x-1][y-1]=1
	ol.put((x-1, y-1))
	al[y-1][x-1]=1
	while not ol.empty():
		#print(ol.qsize())
		fp, tp = ol.get()
		for i, dist in enumerate(al[tp]):
			nd = al[fp][tp] + dist
			if dist > 0 and (al[fp][i] == -1 or al[fp][i] > nd) and fp < i:
				al[fp][i]=nd
				al[i][fp]=nd
				ol.put((fp,i))
			
		fp,tp=tp,fp
		for i, dist in enumerate(al[tp]):
			nd = al[fp][tp] + dist
			if dist > 0 and (al[fp][i] == -1 or al[fp][i] > nd) and fp < i:
				al[fp][i]=nd
				al[i][fp]=nd
				ol.put((fp,i))
			
	
	
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