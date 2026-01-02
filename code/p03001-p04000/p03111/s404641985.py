N, a, b, c = map(int, input().split())
l = [int(input()) for _ in range(N)]
used = [0]*N
global pattern
pattern = []
global ans
ans = float('inf')

def dfs(A):
    global pattern
    global ans
    if len(A) == N:
        pattern.append(A)
        ans = min(ans, MP(A))
        return
    
    for i in range(4):
        A.append(i)
        dfs(A)
        A.pop()

    return 

def MP(A):
    group1 = []
    group2 = []
    group3 = []
    for i in range(N):
        if A[i] == 1:
            group1 += [l[i]]
        elif A[i] == 2:
            group2 += [l[i]]
        elif A[i] == 3:
            group3 += [l[i]]
    if len(group1) == 0 or len(group2) == 0 or len(group3) == 0:
        return float('inf')

    return calc(group1, a)+calc(group2, b)+calc(group3, c)
    
def calc(group, length):
    res = float('inf')
    for i in range(2**len(group)):
        bag = []
        for j in range(len(group)):
            if (i>>j) & 1:
                bag += [group[j]]
        
        if len(bag) == 0:
            continue
        elif len(bag) == 1:
            res = min(res, abs(length - bag[0]))
        else:
            res = min(res, abs(length - sum(group)) + 10*(len(group)-1))
        
    return res

dfs([])
print(ans)
