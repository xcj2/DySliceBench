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
	al.sort(reverse = True)
	ss=sum(al)
	arrive=[0]*k
	arrive[0]=1
	useful_set=set()
	for v in al:
		ss -= v
		u_max=0
		if v >=k:
			useful_set.add(v)
			continue
		for i, _ in enumerate(arrive):
			p = k-i-1
			is_on = arrive[p]
			if is_on==1 and p+v >= k:
				useful_set.add(v)
				u_max=k
			elif is_on==1:
				arrive[p+v] = 1
				u_max=max(u_max, p+v)
		if u_max + ss >= k:
			useful_set.add(v)
	ret=0
	for v in al:
		if v not in useful_set:
			ret += 1
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