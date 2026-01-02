import sys
def solve(balls):
    if distribute(balls, [], []): print('YES')
    else: print("NO")
        
def distribute(balls, R, L):    
    if len(balls) != 0:
        next = balls[0]
        if isMutch(next, R):
            neoR = R
            neoR.append(next)
            if distribute(balls[1:], neoR, L): return True
        
        if isMutch(next, L):
            neoL = L
            neoL.append(next)
            if distribute(balls[1:], R, neoL): return True
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

sys.setrecursionlimit(2**11)
size = int(input());
for i in range(size):
    balls = []
    for a in input().split(' '):
        balls.append(int(a))   
    solve(balls)