import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
mod=1000000007

#+++++

def main():
	#a = int(input())
	n, m = IN()
	#s = input()
	sn=[0]*n
	for i in range(m):
		dd=2 ** i
		al=list(IN())
		for ni in al[1:]:
			sn[ni-1] += dd
	
	switch_aa=list(IN())
	switch_aaa=0
	for i, v in enumerate(switch_aa):
		if v == 1:
			switch_aaa+= 2**i
	
	cc=0
	for state_i in range(2 ** n):
		switch_state=0
		for switch_i, is_on in enumerate(bin(state_i+2**12)[14-n+1:]):
			if is_on == '1':
				switch_state = switch_state ^ sn[switch_i]
		else:
			switch_state = switch_state ^ switch_aaa
			if switch_state == 0:
				cc+=1
	print(cc)
			
		
				
			
			
	
	
	
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