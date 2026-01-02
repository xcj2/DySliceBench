import sys
#import numpy as np

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(IN())
mod=1000000007

#+++++
def ii(v, n):
	v += 2 ** 15
	ret = bin(v)[-n:]
	return ret

def v_sum(a,b):
	return [av+bv for av,bv in zip(a,b)]

def get_n(rr, mm, k, limit):
	ret = sum([int(c) for c in rr])
	o = mm[0]
	pp = []
	for index_i, is_cut in enumerate(rr):
		if is_cut == '1':
			pp.append(o)
			o = mm[index_i+1]
		else:
			o = v_sum(o, mm[index_i+1])
			
		if max(o) > k:
			return mod, None
			
	pp.append(o)
	
	ll = [pp[j][0] for j in range(len(pp))]
	for v in ll:
		if v > k:
			return mod, None
	
	cc = [0]*(len(mm[0]))
	for i in range(1, len(mm[0])):
		for il, v in enumerate(ll):
			if ll[il] + pp[il][i] > k:
				ret += 1
				if ret >= limit:
					return limit+1, None
				ll = [pp[j][i] for j in range(len(pp))]
				cc[i] = 1
				break
			else:
				ll[il] += pp[il][i]
	return ret, cc

def main():
	h, w, k = tin()
	mm=[]
	for _ in range(h):
		s = input()
		s = [int(c) for c in s]
		#s = np.array(s)
		mm.append(s)
		
	n = (h-1)*(w-1) + 1
	for i in range(2 ** (h-1)):
		rr = ii(i, h-1)
		tt, cut_info = get_n(rr, mm, k, n)
		if tt < n:
			n = tt
		
	print(n)
	
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