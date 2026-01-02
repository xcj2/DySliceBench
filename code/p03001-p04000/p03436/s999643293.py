import sys
import queue

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def main():
	#a = int(input())
	h, w = tin()
	#s = input()
	ol = queue.Queue()
	m=[input() for _ in range(h)]
	b = [[-1]*w for _ in range(h)]
	b[0][0]=1
	ol.put(0)
	while not ol.empty():
		p = ol.get()
		x, y = p//1000, p%1000
		for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
			if x+dx<0 or x+dx>=h or y + dy <0 or y+dy >= w:
				continue
			if m[x+dx][y+dy]=='#':
				continue
			if b[x+dx][y+dy]>=0:
				continue
			b[x+dx][y+dy]=b[x][y]+1
			ol.put((x+dx)*1000+(y+dy))
	#print(b)
	if b[-1][-1]==-1:
		return -1
	return sum([s.count('.') for s in m])- b[-1][-1]
		
	
	
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