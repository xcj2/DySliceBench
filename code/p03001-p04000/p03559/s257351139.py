import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def main():
	n = int(input())
	#b , c = tin()
	#s = input()
	al = lin()
	bl = lin()
	cl = lin()
	al.sort()
	bl.sort()
	cl.sort()
	cl_num=bl[:]
	cl_pos=0
	for i, vb in enumerate(bl):
		while cl_pos <n and cl[cl_pos] <= vb:
			cl_pos += 1
		cl_num[i] = n-cl_pos
		
	cl_nokori=[0]*n
	cl_nokori[-1] = cl_num[-1]
	for i, v in enumerate(cl_num[::-1]):
		if i == 0:
			continue
		cl_nokori[n-i-1] = cl_nokori[n-i]+v
	
	ret = 0
	bl_pos=0
	for va in al:
		while bl_pos < n and va >= bl[bl_pos]:
			bl_pos += 1
		if bl_pos == n:
			break
		ret += cl_nokori[bl_pos]
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
