import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def dd(al,n):
	imos=[0]*(n+1)
	for i, v in enumerate(al):
		imos[max(0, i-v)]+=1
		imos[min(n, i+v+1)]-=1
	ret = [0]*(n)
	ret[0]=imos[0]
	mmm=0
	for i, v in enumerate(imos[1:-1],1):
		ret[i]=ret[i-1]+imos[i]
	return ret, min(ret)



def main():
	#a = int(input())
	n, k = tin()
	#s = input()
	al=lin()
	for _ in range(k):
		nal, min_al = dd(al,n)
		if min_al == n:
			print(*nal)
			return
		al=nal
	print(*nal)
	
	
	
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