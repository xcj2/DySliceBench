import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
mod=1000000007

#+++++

def get_cost(min_v,max_v):
	if max_v<0:
		return abs(min_v)
	elif min_v >=0:
		return max_v
	else:
		ret = min(max_v+abs(min_v)*2, abs(min_v)+ max_v*2)
		return ret

def main():
	n, k = IN()
	al=list(IN())
	ret=min([get_cost(a,b) for a,b in zip(al,al[k-1:])])
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