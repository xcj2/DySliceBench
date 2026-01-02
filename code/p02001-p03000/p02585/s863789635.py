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
	n, k = tin()
	#s = input()
	al = lin()
	cl=lin()
	dd=[0]*n
	for i in range(n):
		if dd[i]!=0:
			continue
		cc=set()
		pos = i
		point=0
		n_node=0
		while pos not in cc:
			cc.add(pos)
			pos=al[pos]-1
			point+=cl[pos]
			n_node+=1
			
		for p in cc:
			dd[p] = (point, n_node)
	
	ret=-mod*mod
	for i in range(n):
		pi, ni = dd[i]
		if pi < 0:
			point=0
			pmax=-mod*mod
			pos=i
			for _ in range(ni):
				cc.add(pos)
				pos=al[pos]-1
				point+=cl[pos]
				pmax = max(pmax, point)
			ret = max(ret, pmax)
		elif k < ni*2:
			point=0
			pmax=-mod*mod
			pos=i
			for _ in range(k):
				cc.add(pos)
				pos=al[pos]-1
				point+=cl[pos]
				pmax = max(pmax, point)
			ret = max(ret, pmax)
		else:
			point = pi*((k//ni)-1)
			nk=k%(ni) + ni
			pos = i
			pmax = point
			for _ in range(nk):
				cc.add(pos)
				pos=al[pos]-1
				point+=cl[pos]
				pmax = max(point, pmax)
			ret = max(ret, pmax)
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