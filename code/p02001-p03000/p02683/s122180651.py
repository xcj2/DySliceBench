import sys
sys.setrecursionlimit(700000)

def s_in():
    return input()

def n_in():
    return int(input())

def l_in():
    return list(map(int, input().split()))

n,m,x = l_in()

MAX = 10000000
res = MAX


C = []
A = []
for _ in range(n):
    tmp = l_in()
    c = tmp[0]
    a = tmp[1:]
    C.append(c)
    A.append(a)

stack = []

def evaluate():
    R = [0]*m
    c = 0
    for i, t in enumerate(stack):
        if t == 1:
            c += C[i]
            for j, b in enumerate(A[i]):
                R[j] += b

    if all(r >= x for r in R):
        return c
    else:
        return MAX
            

def do(i):
    tmp = MAX
    for t in [0,1]:        
        stack.append(t)
        if i == n-1:
            tmp = min(tmp, evaluate())
        else:
            tmp = min(tmp, do(i+1))
        stack.pop()
    return tmp

res = do(0)
    
if res == MAX:
    print(-1)
else:
    print(res)
    
