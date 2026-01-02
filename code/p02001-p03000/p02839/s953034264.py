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
	h, w = tin()
	#s = input()
	al = [lin() for _ in range(h)]
	dl = [[abs(a-b) for a,b in zip(all, lin())] for all in al]
	pp = [[set() for _ in range(w)] for _ in range(h)]
	pp[0][0].add(dl[0][0])
	for wi in range(1, w):
		ss = pp[0][wi]
		d = dl[0][wi]
		for v in pp[0][wi-1]:
			ss.add(v+d)
			ss.add(abs(v-d))
	
			
	for hi in range(1, h):
		ss = pp[hi][0]
		gap = dl[hi][0]
		for v in pp[hi-1][0]:
			ss.add(v+gap)
			ss.add(abs(v-gap))
		
		for wi in range(1, w):
			ss = pp[hi][wi]
			gap = dl[hi][wi]
			for v in pp[hi][wi-1]:
				ss.add(v+gap)
				ss.add(abs(v-gap))
			
			for v in pp[hi-1][wi]:
				ss.add(v+gap)
				ss.add(abs(v-gap))
			
	#for hi in range(h):
	#	for wi in range(w):
	#		print(hi,wi,pp[hi][wi])
			
	ret = min(pp[-1][-1])
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