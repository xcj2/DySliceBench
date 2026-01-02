import math,sys,bisect,heapq
from collections import defaultdict,Counter,deque
from itertools import groupby,accumulate
#sys.setrecursionlimit(200000000)
int1 = lambda x: int(x) - 1
input = iter(sys.stdin.buffer.read().decode().splitlines()).__next__
ilele = lambda: map(int,input().split())
alele = lambda: list(map(int, input().split()))
ilelec = lambda: map(int1,input().split())
alelec = lambda: list(map(int1, input().split()))
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
MOD = 1000000000 + 7
def Y(c):  print(["NO","YES"][c])
def y(c):  print(["no","yes"][c])
def Yy(c):  print(["No","Yes"][c])
    
def primeFactors(n): 
	A =set()
	while n % 2 == 0: 
		A.add(2) 
		n = n // 2
	for i in range(3,int(math.sqrt(n))+1,2): 
		while n % i== 0: 
			A.add(i) 
			n = n // i 
	if n > 2: 
		A.add(n) 
	return list(A)


N= int(input())
A = alele()
mark = {}
f1 = 1
f2 = 0
x = None
for i in A:
    if f2 == 0:
        if x == None:
            x=i
        x = math.gcd(x,i)
        if x == 1:
            f2 =1
    if f1 == 1:
        c = primeFactors(i)
        for j in c:
            if mark.get(j,-1) !=-1:
                f1 = 0
                break
            mark[j] = 1
if f1 == 1:
    print("pairwise coprime")
elif f2 == 1:
    print("setwise coprime")
else:
    print("not coprime")

    
    
    