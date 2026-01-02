import copy
import sys
import math

def main():
	n = int(input())
	a = list(map(int,input().split()))
	a.sort()
	tmp = listtodict(a)
	b = {}
	for k,v in tmp.items():
		b[k] = int(v/2)
	b = sorted(b.items(), key=lambda x:x[0])
	w = -1
	for i in reversed(b):
		k=i[0]
		v=i[1]
		if(v>1 and w==-1):
			print(k**2)
			sys.exit()
		elif(v>0 and w==-1):
			w = k
		elif(v>0):
			print(w*k)
			sys.exit()
	print(0)


def listtodict(a):
	b = {}
	for i in a:
		try:
			b[i] += 1
		except:
			b[i] = 1
	return b

def base_10_to_n(X, n):
	X_dumy = X
	out = ''
	while X_dumy>0:
		out = str(X_dumy%n)+out
		X_dumy = int(X_dumy/n)
	if(out == ''): return '0'
	return out

main()