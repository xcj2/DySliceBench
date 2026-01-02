import sys
from collections import defaultdict

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
mod=1000000007

#+++++

def main():
	n = int(input())
	al = list(IN())
	odd_dd=defaultdict(lambda : 0)
	odd_dd[-1]=0
	even_dd=defaultdict(lambda :0)
	even_dd[-1]=0
	
	for i, v in enumerate(al):
		if i%2==0:
			odd_dd[v] += 1
		else:
			even_dd[v] += 1
	
	odd_ll=[(odd_dd[key], key) for key in odd_dd.keys()]
	even_ll=[(even_dd[key], key) for key in even_dd.keys()]
	
	odd_ll.sort(reverse=True)
	even_ll.sort(reverse=True)
	kk=n//2
	pa(odd_ll)
	pa(even_ll)
	
	#先頭が同じ
	if odd_ll[0][1] == even_ll[0][1]:
		ra=(kk-odd_ll[0][0])+(kk-even_ll[1][0])
		rb=(kk-odd_ll[1][0])+(kk-even_ll[0][0])
		return min(ra, rb)
	else:
		ret= (kk-odd_ll[0][0])+(kk-even_ll[0][0])
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