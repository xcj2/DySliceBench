import sys

input_methods=['clipboard','file','key']
using_method=1
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
mod=1000000007

#+++++

def next(v, cu):
	for i in cu:
		if i > v:
			return i
	else:
		return -1

def main():
	n, k = IN()
	al = list(IN())
	cu=[]
	for i in range(10):
		if i not in al:
			cu.append(i)
	non_zero_min = cu[0] if cu[0] > 0 else cu[1]
	is_cu0_is_0 = cu[0]==0
	
	if n < 10:
		if n in cu:
			return n
		if n > cu[-1]:
			return non_zero_min*10+cu[0]
	
	kiriage=False
	ret=[]
	for i, v in enumerate(str(n)):
		if kiriage:
			ret.append(cu[0])
		elif int(v) in cu:
			ret.append(v)
		else:
			kiriage=True
			n = next(int(v),cu)
			if n == -1:
				if i != 0:
					ret.append(cu[0])
				else:
					ret.append(str(non_zero_min)+str(cu[0]))
				
				for ic in range(i-1,-1,-1):
					#print(ic)
					t=ret[ic]
					nt = next(int(t),cu)
					if nt != -1:
						#print('a', nt, int(t))
						ret[ic]=nt
						break
					elif nt == -1 and ic == 0:
						ret[ic]=str(non_zero_min)+str(cu[0])
						#print(ret)
					else:
						ret[ic]=cu[0]
			else:
				ret.append(n)
	return ''.join([str(r) for r in ret])
			
			
			
			
			
	
	
	
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