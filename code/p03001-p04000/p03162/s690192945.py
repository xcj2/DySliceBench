from sys import stdin,stdout,setrecursionlimit
from collections import Counter as C
setrecursionlimit(10**6)
M = 1000000007
input = stdin.readline
def write(n,sep="\n"):
	stdout.write(str(n))
	stdout.write(sep)
def gil():
	return list(map(int, input().split()))
	
n = int(input())
a, b, c = [], [], []
for i in range(n):
    x,y,z = gil()
    a.append(x)
    b.append(y)
    c.append(z)
    
mem = [[-1 for _ in range(3)] for _ in range(n+1)]
def rp(i, p):
    global a,b,c,n
    if i >= n:
        return 0
    if mem[i][p] != -1:
        return mem[i][p]
    av = [a[i] + rp(i+1, 0), b[i] + rp(i+1, 1), c[i] + rp(i+1, 2)]
    if p != -1:
        av[p] = 0
    ans = max(av)
    mem[i][p] = ans
    return ans
ans = rp(0, -1)
print(ans)
        
    
# on recursive mem sols, build the solution from the base case,
# ie, return 0 on basecase, and build up the solution.
# because state-cases below will not carry values from above, they only take values from below


