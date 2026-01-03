import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
mod=1000000007

#+++++

def can_set(al_max ,k,cc):
	a=al_max
	aa=((k//(cc+1))*cc) + (k%(cc+1))
	#pa((a,cc,aa))
	if a <= aa:
		return True
	return False

def main():
	k, t = IN()
	al = list(IN())
	al.sort(reverse=True)
	#pa(al)
	
	#if al[0] <= (k+1)//2:
	#	return 0
	#if al[0] == k:
	#	return k-1
	tt=sum(al)
	mm=al[0]
	nokori=tt-mm
	ret = max(0, tt - nokori*2-1)
	print(ret)
	
	

def main2():
	k, t = IN()
	al = list(IN())
	al.sort(reverse=True)
	ttt=[0]*k
	p=0
	for i, v in enumerate(al):
		for _ in range(v):
			ttt[p]=i
			p+=2
			if p >= k:
				p=1
	
	cc=0
	pre=-1
	for v in ttt:
		if pre == v:
			cc+=1
		else:
			pre=v
			
	return cc
	
	
	
	
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