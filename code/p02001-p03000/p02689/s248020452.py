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
n,m = invr()
nums = [0] + inlt()
graph = defaultdict(set)

for i in range(m):
    a,b = invr()
    graph[a].add(b)
    graph[b].add(a)

cnt = 0
for i in range(1,n + 1):
    for each in graph[i]:
        if nums[i] <= nums[each]:
            break
    else:
        cnt += 1
print(cnt)

