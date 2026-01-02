a = [int(i) for i in input().split()]

def loss(a):
    maxItem = max(a)
    s = 0
    for i in a:
        s+=abs(i-maxItem)
    return s

def inctwo(a):
    maxidx = a.index(max(a))
    copy = list(a)
    for i in range(3):
        if i!=maxidx:
            copy[i]+=1
    return [copy,loss(copy)]

def incone(a):
    minItem = a.index(min(a))
    copy = list(a)
    copy[minItem]+=2
    return [copy,loss(copy)]

def solve(a,ans):
    if loss(a)==0:
        return ans
    one = inctwo(a)
    two = incone(a)
    if one[1]==0 or two[1]==0:
        return ans+1
    if one[1]>two[1]:
        return solve(two[0],ans+1)
    else:
        return solve(one[0],ans+1)

print(solve(a,0))
