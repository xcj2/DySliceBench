n = int(input())
a = [0]*n
x = [[0] *n for i in range(n)]
y = [[0] *n for i in range(n)]
ans = 0
for i in range(n):
    a[i] = int(input())
    for j in range(a[i]):
        x[i][j],y[i][j] = map(int,input().split())
        x[i][j]-=1
def honest(i,j):
    return (i>>j)%2 ==1
def check(m):
    for i in range(n):
        if not honest(m,i) :continue
        for j in range(a[i]):
            if y[i][j] == 1 and honest(m,x[i][j]) == 0:
                return False
            if y[i][j] == 0 and honest(m,x[i][j]) == 1:
                return False
    return True
def count(c):
    cnt = 0
    for i in range(c//2+5):
        cnt+= (c >> i)%2
    return cnt
for i in range(2**n):
    if check(i):
        ans = max(ans,count(i))
    
        
        
        
print(ans)
        
