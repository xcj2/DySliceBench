import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=998244353

#+++++

def main():
	# = int(input())
	n, k = tin()
	#s = input()
	al = []
	for _ in range(k):
		l,r = tin()
		al.append([l,r])
	
	dd = [0]*(n)
	dd[0] = 1
	
	ruiseki=[0]*(n)
	ruiseki[0]=1
	ruiseki[1]=-1
	rui=0
	for pos, num in enumerate(ruiseki):
		rui += ruiseki[pos]
		rui %= mod
		dd[pos]=rui
		for l,r in al:
			if pos + l < n:
				ruiseki[pos+l] += rui
			if pos + r + 1 < n:
				ruiseki[pos + r + 1] -= rui
		#pa(dd)
		#pa(ruiseki)
		
	return rui%mod
		
		
	
	
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