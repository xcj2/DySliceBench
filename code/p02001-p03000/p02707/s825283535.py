
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
nums = inlt()
num_dict = defaultdict(int)
for i in range(n - 1):
    num_dict[nums[i]] += 1

for i in range(1,n + 1):
    print(num_dict[i])
    
#print(n - s if s <= n else -1)
#print('No')
#print()

