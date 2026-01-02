

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
n,m = invr()
nums = inlt()
standard = (sum(nums))/(4*m)
nums.sort(reverse = True)
has = True
index = 0
while index < m:
    if nums[index] < standard:
        has = False
        break
    index += 1
if has:
    print('Yes')
else:
    print('No')
#print()
