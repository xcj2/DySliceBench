import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**5) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

funcs = [add, sub]
n,m = li()

xyz = [tuple(li()) for _ in range(n)]

ans = 0
for func1 in funcs:
    for func2 in funcs:
        for func3 in funcs:
            temp = []
            for x,y,z in xyz:
                temp.append(func1(0, func2(x, func3(y, z))))
            
            temp.sort(reverse=True)
            ans = max(ans, sum(temp[:m]))
            
print(ans)