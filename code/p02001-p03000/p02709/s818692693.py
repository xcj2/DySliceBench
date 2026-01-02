import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
mod=1000000007

#+++++

def main():
	n = int(input())
	al = list(IN())
	#b , c = IN()
	#s = input()
	tl=[(v,i+1) for i,v in enumerate(al)]
	tl.sort(reverse=True)
	#print(tl)
	th = lambda f,t:100000*f + t
	fh = lambda hv : (hv//100000, hv%100000)
	
	ss = th(1,n)
	dd={ss:0}
	for uresisa, pos in tl:
		ndd={}
		for dk in dd:
			pu=dd[dk]
			f, t =fh(dk)
			temp_dkf = uresisa*abs(f-pos)+pu
			h=th(f+1, t)
			if h not in ndd:
				ndd[h] = temp_dkf
			else:
				ndd[h] = max(ndd[h], temp_dkf)
			
			temp_dkt = uresisa*abs(t-pos)+pu
			h=th(f, t-1)
			if h not in ndd:
				ndd[h]=temp_dkt
			else:
				ndd[h]=max(ndd[h], temp_dkt)
		else:
			dd=ndd
			#for d in dd:
			#	print(d, dd[d])
			
	rr=0
	for d in dd:
		rr=max(rr, dd[d])
	return rr
			
	
	
	
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