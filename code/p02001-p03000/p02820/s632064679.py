n,k = list(map(int,input().split()))
r,s,p = list(map(int,input().split()))
t = input()

def opt(c):
    if c=='r':
        return 'p'
    if c=='s':
        return 'r'
    if c=='p':
        return 's'

def sec(c,x):
    if x!=opt(c):
        return opt(c)
    else:
        return 'x'
    
def cnt(ans):
    c = 0
    for i in range(len(ans)):
        if ans[i]=='r':
            c+=r
        if ans[i]=='s':
            c+=s
        if ans[i]=='p':
            c+=p
    return c


ans = ""
for i in range(len(t)):
    if i-k>=0:
        ans+=sec(t[i],ans[i-k])
    else:
        ans+=opt(t[i])
        
print(cnt(ans))