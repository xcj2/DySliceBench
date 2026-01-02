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
nums = [0] + inlt()
cycle = [nums[1]]
s = set([cycle[0]])
bp = 0
for i in range(2*n):
    if nums[cycle[-1]] not in s:
        s.add(nums[cycle[-1]])
        cycle.append(nums[cycle[-1]])
        
    else:
        bp = nums[cycle[-1]]
        break

if k <= len(cycle):
    print(cycle[k - 1])
else:
    if bp != 0:
        for i in range(len(cycle)):
            if cycle[i] == bp:
                cycle = cycle[i:]
                break
    k -= i
    remain = k % len(cycle)
    print(cycle[remain - 1])

    
