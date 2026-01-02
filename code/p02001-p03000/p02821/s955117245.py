import sys

input_methods=['clipboard','file','key']
using_method=1
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
mod=1000000007

#+++++


def count_al(al, vv):
	#'''
	#vvv以上を集めた場合、何要素選択されるか。
	#'''
	rui=0
	for v in al:
		r = get_ok_index(v, al, vv)
		rui += r
	return rui

def get_ok_index(v,al,ok_value):
	#'''
	#ok_value以上の要素数を返す。
	#'''
	if v+al[0] < ok_value:
		return 0
	if v + al[-1] >= ok_value:
		return len(al)
	ok=0
	ng=len(al)
	while ok + 1 < ng:
		#pa((ok,ng))
		m=(ok+ng)//2
		if v+al[m] >= ok_value:
			ok = m
		else:
			ng = m
		#pa((ok,ng))
	return ok+1
	

def main():
	n, m = IN()
	al = list(IN())
	al.sort(reverse=True)
	if m == n*n:
		ret= sum(al) * n * 2
	
	ruisekiwa=al[:]
	for i,v in enumerate(al[1:],1):
		ruisekiwa[i]=ruisekiwa[i-1]+v
	#pa(ruisekiwa)
		
	ok=al[0]*10
	ng=0
	
	while ok  > ng + 1:
		vv = (ok + ng)//2
		cc = count_al(al, vv)
		#pa(('ok,ng,vv,cc',ok,ng,vv,cc))
		if cc <= m:
			ok = vv
		else:
			ng = vv
	#pa(('ok',ok))
	
	ret=0
	for v in al:
		ok_id = get_ok_index(v, al, ok)-1
		#pa(ok_id)
		if ok_id==-1:
			continue
		ret += ruisekiwa[ok_id]+v*(ok_id+1)
	
	ret += (ok - 1)*(m-count_al(al,ok))
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