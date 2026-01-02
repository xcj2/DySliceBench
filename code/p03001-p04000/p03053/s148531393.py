import sys
#import queue

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

class queue:
	def __init__(self):
		self.l=[0]*(1000*1000+100)
		self.f=0
		self.t=0
		
	def put(self,v):
		self.l[self.f]=v
		self.f+=1
		
	def get(self):
		self.t+=1
		return self.l[self.t-1]
		
	def empty(self):
		return self.f==self.t

def main():
	#a = int(input())
	h, w = tin()
	#s = input()
	mp = [list(input()) for _ in range(h)]
	dist=[[-1] * w for _ in range(h)]
	open_list=queue()
	for hi, l in enumerate(mp):
		for wi, c in enumerate(l):
			if c == '#':
				dist[hi][wi]=0
				open_list.put(hi*2000+wi)
				
	max_dist=0
	while not open_list.empty():
		hi_wi = open_list.get()
		hi = hi_wi // 2000
		wi = hi_wi % 2000
		d = dist[hi][wi]
		for dw, dh in [(0,1),(0,-1),(1,0),(-1,0)]:
			if -1 == wi+dw or -1 == hi + dh or w == wi+dw or h == hi + dh:
				continue
			if dist[hi+dh][wi+dw] >= 0:
				continue
			#if dist[hi+dh][wi+dw]==-2:
				
			dist[hi+dh][wi+dw]=d+1
			open_list.put(((hi+dh)*2000+wi+dw))
			max_dist=d+1
	print(max_dist)
	#for l in dist:
	#	print(l)
	
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
		input = sys.stdin.readline
			
	ret = main()
	if ret is not None:
		print(ret)