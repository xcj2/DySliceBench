from math import gcd

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
n = inp()
nums = [0] + inlt()
dp = [0 for i in range(n + 1)]
s = [0 for i in range(n + 1)]
s[1] = nums[1]
for i in range(3,n,2):
    s[i] = s[i - 2] + nums[i]
if n == 1:
    print(nums[0])
elif n == 2:
    print(max(nums[1],nums[2]))
elif n == 3:
    print(max(nums[3],nums[1],nums[2]))
elif n == 4:
    print(max(nums[1] + nums[3],nums[1] + nums[4],nums[2] + nums[4]))
else:
    dp[1] = nums[1]
    dp[2] = max(nums[1],nums[2])
    dp[3] = max(nums[3],nums[1],nums[2])
    dp[4] = max(nums[1] + nums[3],nums[1] + nums[4],nums[2] + nums[4])
    for i in range(5,n + 1):
        if i % 2 == 0:
            dp[i] = max(dp[i - 2] + nums[i], s[i - 1]) #if n % 2 == 0 take sum else dp[i - 1]
        else:
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    print(dp[n])
#print('No')
#print()
