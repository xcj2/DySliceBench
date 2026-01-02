import sys

input_methods=['clipboard','file','key']
using_method=1
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

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

#####segfunc######
def segfunc(x,y):
   return min(x,y)

def init(init_val):
    #set_val
    for i in range(n):
        seg[i+num-1]=init_val[i]    
    #built
    for i in range(num-2,-1,-1) :
        seg[i]=segfunc(seg[2*i+1],seg[2*i+2]) 
    
def update(k,x):
    k += num-1
    seg[k] = x
    while k:
        k = (k-1)//2
        seg[k] = segfunc(seg[k*2+1],seg[k*2+2])
    
def query(p,q):
    if q<=p:
        return ide_ele
    p += num-1
    q += num-2
    res=ide_ele
    while q-p>1:
        if p&1 == 0:
            res = segfunc(res,seg[p])
        if q&1 == 1:
            res = segfunc(res,seg[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = segfunc(res,seg[p])
    else:
        res = segfunc(segfunc(res,seg[p]),seg[q])
    return res

#####単位元######
ide_ele = 0

#num:n以上の最小の2のべき乗
#num =2**(n-1).bit_length()
#seg=[ide_ele]*2*num


n, k = tin()
#al = [int(input()) for _ in range(n)]
v_max = 300000
mmv = [0] * (v_max+1)
num=2**(v_max-1).bit_length()
seg = [ide_ele]*2*num

#init(mmv)
for value_i in range(n):
	value_i=int(input())
	r = query(max(value_i-k,0), min(value_i+1+k,v_max+1))
	update(value_i, r-1)
v = -query(0, num)
print(v)

	
