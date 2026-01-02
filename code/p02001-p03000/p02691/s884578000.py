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
n = inp()
nums = [0] + inlt()
num_dict = defaultdict(int)
cnt = 0
for i in range(1,n + 1):
    num_dict[i - nums[i]] += 1

for i in range(1,n + 1):
    ii = i + nums[i]
    jj = i - nums[i]
    if num_dict[jj] > 0:
        num_dict[jj] -= 1
    cnt += num_dict[ii]
    

print(cnt)

