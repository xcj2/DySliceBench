import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
mod=1000000007

#+++++

def get_n(a_c):
	return ord(a_c)-ord('a')

def main():
	h,w  = IN()
	dd=[0]*(get_n('z')+1)
	for _ in range(h):
		s = input()
		for c in s:
			v=get_n(c)
			dd[v] += 1
			
	pa(dd)
	mmmd=[0]*4
	for v in dd:
		mmmd[v%4]+=1
	
	pa(mmmd)
	th_1_3=(h%2)*(w%2)
	th_2=(h%2)*(w//2)+(w%2)*(h//2)
	pa(th_2)
	if mmmd[1]+mmmd[3] > th_1_3:
		return 'No'
	if mmmd[2] > th_2:
		return 'No'
	return 'Yes'
	
	
	
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