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
	m = []
	for _ in range(h):
		s = input()
		m.append(s)
	ret = [['#']*w for _ in range(h)]
	
	for hi in range(h):
		for wi in range(w):
			p=0
			if m[hi][wi]=='#':
				continue
			for dh in [1, 0, -1]:
				if hi+dh < 0 or hi+dh >= h:
					continue
				for dw in [1, 0, -1]:
					if wi+dw < 0 or wi+dw >= w:
						continue
					if dh == 0 and dw == 0:
						continue
					if m[hi+dh][wi+dw]=='#':
						p+=1
			ret[hi][wi]=p
	for v in ret:
		print(''.join([str(i) for i in v]))
	
	
	
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