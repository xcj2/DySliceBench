import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
mod=1000000007

#+++++

def main():
	n = int(input())
	dd=[[] for i in range(n)]
	
	
	for i in range(n-1):
		na, nb , dist = IN()
		dd[na-1].append((nb-1, dist))
		dd[nb-1].append((na-1, dist))
	#parent, parent_color, current, dist
	
	stock=[(0,0,0)]
	ret=[0]*n
	
	while len(stock)>0:
		(pn, cn, cc) = stock.pop()
		#pa(len(stock))
		#print(pn,pc,cn,di)
		for next_n, dist in dd[cn]:
			if next_n==pn:
				continue
				
			paint_color = cc
			if dist % 2 == 1:
				paint_color = (cc + 1)%2
			ret[next_n] = paint_color
			stock.append((cn, next_n,paint_color))
			
	for color in ret:
		print(color)
	
	
	
	
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