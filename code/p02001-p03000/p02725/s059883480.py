

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
k,n = invr()
nums = inlt()
ans = min(nums[-1] - nums[0],k - (nums[1] - nums[0]))
for i in range(1,n - 1):
    
    result = min(k - (nums[i] - nums[i - 1]), \
             k - abs(nums[i + 1] - nums[i]))
    #print(i,result)
    if result < ans:
        ans = result

ans = min(ans,k - (nums[-1] - nums[-2]))
print(ans)
