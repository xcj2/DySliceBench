pi = 3.1415926

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
n,k = invr()
ans = [0 for i in range(n)]
cnt = 0
for i in range(k):
    d = inp()
    nums = inlt()
    for j in nums:
        ans[j - 1]= 1

for i in ans:
    if i == 0:
        cnt += 1

print(cnt)

