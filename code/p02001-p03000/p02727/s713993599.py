import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
mod=1000000007

#+++++

def main():
	#a = int(input())
	x, y, a, b, c = IN()
	al = list(IN())
	al.sort(reverse=True)
	bl = list(IN())
	bl.sort(reverse = True)
	cl = list(IN())
	cl.sort(reverse=True)
	#s = input()
	tx=x-1
	ty=y-1
	tc=0
	while True:
		if tc == len(cl):
			break
		al_min=al[tx] if tx >= 0 else 10**11
		bl_min=bl[ty] if ty >= 0 else 10**11
		cl_max=cl[tc]
		if al_min >= cl_max and bl_min >= cl_max:
			break
		elif al_min <= bl_min and al_min < cl_max:
			tx -= 1
			tc += 1
		elif bl_min<= al_min and bl_min < cl_max:
			ty -= 1
			tc += 1
		else:
			break
	ret=sum(al[:tx+1])+sum(bl[:ty+1])+sum(cl[:tc])
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