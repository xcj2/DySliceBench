K=int(input())

ans = [0]

def hoge(n):
    global ans
    if ans[-n] != 9:
        ans[-n]+=1
        if check():
            pass
        else:
            huga(n)
    else:
        if len(ans) < n+1:
            ans = [0] * (n+1)
            ans[0] = 1
        else:
            huga(n)

def huga(n):
    global ans
    ans[-(n+1)]+=1
    for i in range(n,0,-1):
        if(ans[-(i+1)]==0):
            ans[-i] = 0
        else:
            ans[-i]=ans[-(i+1)]-1
    ans[-(n+1)]-=1
    hoge(n+1)


def check():
    global ans
    for i in range(len(ans)-1):
        if abs(ans[i]-ans[i+1])>1:
            return False
    return True
       


for i in range(K):
    hoge(1)
print(''.join(map(str,ans)))
