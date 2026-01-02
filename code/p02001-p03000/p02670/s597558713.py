import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

#+++++

def main():
	n = int(input())
	nn = [[min(i,j,n-i-1,n-j-1) for j in range(n)] for i in range(n)]
	is_sit = [[True] * n for _ in range(n)]
	cc = [[0]*n for _ in range(n)]
	
	#b , c = tin()
	pl = list(map(int, input().split()))
	ans = 0
	for p in pl:
		x, y = (p-1) // n, (p-1) % n
		ans += nn[x][y]
		is_sit[x][y] = False
		q = [(x, y, nn[x][y])]
		while q:
			(x, y, v) = q.pop()
			if x >= 0 and nn[x-1][y]>v:
				nn[x-1][y] = v
				q.append((x-1, y, v+is_sit[x-1][y]))
			if x < n-1 and nn[x+1][y]>v:
				nn[x+1][y] = v
				q.append((x+1, y, v+is_sit[x+1][y]))		
			if y >= 0 and nn[x][y-1]>v:
				nn[x][y-1] = v
				q.append((x, y-1, v+is_sit[x][y-1]))
			if y < n-1 and nn[x][y+1]>v:
				nn[x][y+1] = v
				q.append((x, y+1, v+is_sit[x][y+1]))	
		
	print(ans)
	#s = input()	
	
	
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
		input = sys.stdin.readline
			
	ret = main()
	if ret is not None:
		print(ret)
