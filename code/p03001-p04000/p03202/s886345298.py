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

def shave(stack:list, nex:int, prv:int):
    res = prv-nex
    while res > 0:
        if res >= stack[-1][1]:
            _,y = stack.pop()
            res -= y
        else:
            stack[-1][1] -= res
            res = 0
            

def normalize(stack: list):
    if stack[-1][0] == stack[-2][0]:
        stack[-2][1] += stack[-1][1]
        stack.pop()
        
def add(stack:list):
    if stack[-1][1] == 1:
        stack[-1][0] += 1
    else:
        stack[-1][1] -= 1
        stack.append([stack[-1][0]+1, 1])
        
def kuriagari(stack:list):
    _, y = stack.pop()
    add(stack)
    normalize(stack)
    stack.append([1,y])
    
def check(a:list, upto:int):
    stack = [[0,0]]
    for i in range(n):
        if a[i+1] > a[i]:
            stack.append([1, a[i+1]-a[i]])
            normalize(stack)
        else:
            shave(stack, a[i+1], a[i])
            
            if stack[-1][0] == upto and stack[-1][1] == a[i+1]:
                return False

            elif stack[-1][0] == upto:
                kuriagari(stack)
            
            else:
                add(stack)
                normalize(stack)
                
    return True
   
    
def binsearch(a:list):
    low = 0
    high = 10**9+1
    
    while high-low > 1:
        mid = (high+low) // 2
        if check(a, mid):
            high = mid
        else:
            low = mid
            
    return high

n = ni()
a = [0] + list(li())
ans = binsearch(a)
print(ans)