import sys

def solve(balls):
    ans = distribute(balls, [], [])
    if ans is True: print('YES')
    else: print("NO")
        
def distribute(balls, R, L):    
    if len(balls) != 0:
        next = balls[0]
        ans = False
        #case R
        if isMutch(next, R):
            neoR = R
            neoR.append(next)
            ans = distribute(balls[1:], neoR, L)
        if ans: return True
        
        if isMutch(next, L):
            neoL = L
            neoL.append(next)
            ans =distribute(balls[1:], R, neoL)
        if ans: return True
    else:
        return isOrdered(R) and isOrdered(L)

def isMutch(next, lis):
    if len(lis) != 0:
        return next >= lis[len(lis)-1]
    return True
    
def isOrdered(lis):
    #check both R and L are ordered
    checker = sorted(lis)
    return checker == lis
  
limit = 2**11
sys.setrecursionlimit(limit)
  
line = input()
size = -1;
while True:
    if size == -1:
        size = int(line)
    else:
        balls = []
        for a in line.split(' '):
            balls.append(int(a))   
        solve(balls)
        size -= 1
        if size == 0: break
    line = input()