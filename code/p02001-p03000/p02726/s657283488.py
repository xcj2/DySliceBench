from collections import defaultdict

############ ---- USER DEFINED INPUT FUNCTIONS ---- ############
def inp():
    return(int(input().rstrip()))
def inlt():
    return(list(map(int,input().rstrip().split())))
def insr():
    s = input().rstrip()
    return(s[:len(s) - 1])
def invr():
    return(map(int,input().rstrip().split()))
################################################################
n,X,Y = invr()
ans = defaultdict(int)

for i in range(1,n):
    for j in range(i + 1,n + 1):
        if i < X:
            if j > Y:
                result = min(j - i,(X-i) + (j - Y) + 1)
            else:
                result = min(j - i,(X-i) + (Y - j) + 1)
        else:
            if j > Y:
                result = min(j - i,(i - X) + (j - Y) + 1)
            else:
                result = min(j - i,(i - X) + (Y - j) + 1)
        ans[result] += 1
    

for i in range(1,n):
    print(ans[i])
