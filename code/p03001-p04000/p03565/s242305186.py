import sys

input_methods=['clipboard','file','key']
using_method=1
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
mod=1000000007

#+++++

def is_ok(sd, st, t):
	if len(sd) < st+len(t):
		return False
	for i, c in enumerate(sd[st:st+len(t)]):
		if c != '?' and t[i] != c:
			return False
	return True
	
def to_aaa(a_str):
	rr=list(a_str)
	for i, c in enumerate(rr):
		rr[i] = 'a' if c == '?' else c
	ret = ''.join(rr)
	return ret

def mk_s(a_s_dash, i, t):
	front = to_aaa(a_s_dash[:i])
	back = to_aaa(a_s_dash[i+len(t):])
	ret = front+t+back
	#pa((i,t,front,t,back,ret))
	return ret
			
def main():
	s_dash = input()
	t=input()
	dd='UNRESTORABLE'
	qq='?'
	
	aa=[]
	for i, _ in enumerate(s_dash[:len(s_dash)+1]):
		#pa((s_dash,i,t))
		if is_ok(s_dash,i,t):
			aa.append(mk_s(s_dash, i, t))
			#pa(aa)
			
	if len(aa)>0:
		aa.sort()
		ret = aa[0]
		print(ret)
		return
		
	print(dd)
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