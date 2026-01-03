import sys
import collections

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def ns(i_s, i_d, other_s, other_d):
	#i_sの方が小さいとしておく。
	if i_s > other_s:
		i_s, i_d, other_s, other_d = other_s, other_d, i_s, i_d
	
	r = i_s
	other_s -= i_s
	if other_s >= i_d:
		r += i_d
		r += other_d // 2
	else:
		r += other_s
		i_d -= other_s
		r += i_d // 2
		r += other_d // 2
	#print(r)
	return r

def nss(aa, ab):
	r = (aa+ab) // 2
	#pa(r)
	return r

def main():
	#a = int(input())
	n,m = tin()
	#s = input()
	al=lin()
	dd=[0]*m
	ni=[0]*m
	cc = collections.Counter(al)
	for k in cc:
		#pa((k,cc[k]))
		nv = cc[k]
		dd[k%m] += nv%2
		ni[k%m] += nv-(nv%2)
	#pa(dd)
	#pa(ni)
	ret = 0
	for i in range(m):
		other = (m-i) % m
		if other < i:
			continue
		#pa((i,other))
		if i == other:
			ret += nss(dd[i], ni[i])
		else:
			ret += ns(dd[i], ni[i], dd[other], ni[other])
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