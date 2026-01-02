import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
mod=1000000007

#+++++

def main():
	a, b, c, d, e, f = IN()
	mm=f
	ww_list=[0]*(mm+1)
	ww_list[0]=1
	for i, is_ok in enumerate(ww_list):
		if is_ok == 1:
			if i+(a*100) <= mm:
				ww_list[i+(a*100)]=1
			if i+(b*100) <= mm:
				ww_list[i+(b*100)]=1
				
	max_noudo=0
	ret_sw=a*100
	ret_suger=0
	for wv, is_ok_w in enumerate(ww_list):
		if is_ok_w == 0:
			continue
		suger_limit=e*(wv//100)
		ok_s=[0]*(suger_limit + 1)
		ok_s[0]=1
		max_suger=0
		for i, is_ok in enumerate(ok_s):
			if is_ok == 1:
				if i + c <= suger_limit and (wv+i+c) <= f:
					ok_s[i+c]=1
					max_suger=max(max_suger, i+c)
				if i+d <= suger_limit and (wv+i+d) <= f:
					ok_s[i+d]=1
					max_suger = max(max_suger, i+d)
		if wv == 0:
				continue
			
		suger_noudo=((100*max_suger)/(wv+max_suger))
		if max_noudo < suger_noudo:
			max_noudo=suger_noudo
			ret_sw = wv+max_suger
			ret_suger = max_suger
	print(ret_sw, ret_suger)
	return 
				
		
	
	

	
	
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