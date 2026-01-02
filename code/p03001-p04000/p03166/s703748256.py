import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
LIN=lambda : list(IN())
mod=1000000007

#+++++

def main():
	#a = int(input())
	n, m = IN()
	#s = input()
	nokori = [0]*n
	max_path_from = [0]*n
	path = []
	tl = [[] for _ in range(n)]
	for _ in range(m):
		f, t = IN()
		f,t=f-1, t-1
		path.append((f,t))
		nokori[t] += 1
		tl[f].append(t)
	sl=[i for i, v in enumerate(nokori) if v == 0]
	mp=0
	while len(sl) > 0:
		next_l = []
		for v in sl:
			for t in tl[v]:
				nokori[t] -= 1
				if nokori[t] == 0:
					next_l.append(t)
		sl = next_l
		mp+=1
	print(mp-1)
		
	
	
	
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