import sys
sys.setrecursionlimit(2000)
input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(float, input().split())
LIN=lambda : list(IN())
mod=1000000007

#+++++

def main():
	n = int(input())
	#b , c = IN()
	#s = input()
	al = LIN()
	#p[i][j]は、i番目までにj枚が表になっている確率をあらわす。
	p = [[0]*(n+1) for _ in range(n+1)]
	p[0][0]=1
	for i in range(1, n+1):
		for j in range(n+1):
			omote = al[i-1]
			ura = 1 - omote
			p[i][j] += p[i-1][j]*ura
			if j > 0:
				p[i][j] += p[i-1][j-1]*omote
	k = p[-1][(n+1)//2:]
	#pa(k)
	r = sum(k)
	print(r)


memo_s=[]
al=[1,1]
n=1
def cc(state, maisuu):
	nokori = n-state
	if maisuu==0:
		return 1
	if nokori < maisuu:
		return 0
	global memo_s
	k = memo_s[state][maisuu]
	if k >= 0:
		return k
	
	omote = al[state]
	ura = 1-omote
	r = cc(state+1, maisuu-1)*omote
	r += cc(state+1, maisuu)*ura
	
	memo_s[state][maisuu]=r
	return r
	
def main2():
	global n
	n = int(input())
	global memo_s
	memo_s = [[-1]*(n+1) for _ in range(n+1)]
	
	v = LIN()
	global al
	al=v[:]
	
	r = cc(0, (n+1)//2)
	print(r)
	
	
	
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