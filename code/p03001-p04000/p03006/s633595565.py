import sys
import collections

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def main():
	n = int(input())
	dd=[]
	for _ in range(n):
		b , c = tin()
		dd.append([b,c])
	#s = input()
	dist_dict=collections.defaultdict(lambda :0)
	for i,(xa, ya) in enumerate(dd):
		for xb, yb in dd:#[i+1:]:
			if xa==xb and ya == yb:
				continue
			dist_dict[str(xa-xb)+'_'+str(ya-yb)]+=1
			dist_dict[str(xb-xa)+'_'+str(yb-ya)]+=1
	rr=0
	for k in dist_dict:
		rr=max(rr,dist_dict[k])
		#print(k,dist_dict[k])
	return n-int(rr//2)
		
	
	
	
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