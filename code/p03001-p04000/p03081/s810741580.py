n,q = map(int,input().split())
s = input()
word = list(s)
li = [list(input().split()) for _ in range(q)]
memo = {}

def dfs(m):
    k = m
    if m in memo:
        return memo[m]
    for t,d in li:
        if word[m] == t:
            if d == 'R':
                m += 1
            else:
                m -= 1
        if m < 0:
            memo[k] = 'Left'
            return 'Left'
        elif m > n-1:
            memo[k] = 'Right'
            return  'Right'
    memo[k] = True
    return True

def left(a,b):
    m = int((a+b)/2)
    if a == m:
        return b
    if dfs(m) == 'Left':
        return left(m,b)
    else:
        return left(a,m)

def right(a,b):
    m = int((a+b)/2)
    if a == m:
        return a
    if dfs(m) == 'Right':
        return right(a,m)
    else:
        return right(m,b)

if dfs(0) == 'Right':
    print(0)
elif dfs(0) == 'Left':
    if dfs(n-1) == 'Right':
        print(right(0,n-1) - left(0,n-1) + 1)
    elif dfs(n-1) == 'Left':
        print(0)
    else:
        print(n - left(0,n-1))
else:
    if dfs(b) == 'Right':
        print(right(0,n-1) + 1)
    elif dfs(b) == 'Left':
        print(0)
    else:
        print(n)
