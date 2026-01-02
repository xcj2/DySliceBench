N,X=map(int,input().split())
def burgerLength(n):
    return(pow(2,n+2)-3)
def allpatNum(level):
    return(pow(2,level+1)-1)
def pat(level,x):
    if level == 0:
        if x==0:
            return(0)
        else:
            return(1)
    L = burgerLength(level-1)
    if x == 1:
        ans = 0
    elif x <= 1 + L:
        ans = pat(level-1,x-1)
    elif x == 2 + L:
        ans = allpatNum(level-1) + 1
    elif x < 2 + L + L:
        ans = allpatNum(level-1) + 1 + pat(level-1,x-(2+L))
    else:
        ans = allpatNum(level)
    return(ans)
print(pat(N,X))