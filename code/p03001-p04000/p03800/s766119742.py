import collections

res = str()

def make(ans,n,s):
    for i in range(2,n):
        if ans[i-1] == 'S':
            if s[i-1] == 'o':
                ans += ans[i-2]
            else:
                ans += 'S' if ans[i-2] == 'W' else 'W'
        else:
            if s[i-1] == 'o':
                ans += 'S' if ans[i-2] == 'W' else 'W'
            else:
                ans += ans[i-2]
    return ans

def check(ans,s,i):
    if ans[i] == 'S':
        if s[i] == 'o':
            return ans[i-1] == ans[i+1]
        else:
            return ans[i-1] != ans[i+1]
    else:
        if s[i] == 'o':
            return ans[i-1] != ans[i+1]
        else:
            return ans[i-1] == ans[i+1]

def solve():
    n = int(input())
    s = input()
    ans = make("SS",n,s)
    if check(ans,s,0) and check(ans,s,-1):
        print(ans)
        return
    ans = make("SW",n,s)
    if check(ans,s,0) and check(ans,s,-1):
        print(ans)
        return
    ans = make("WS",n,s)
    if check(ans,s,0) and check(ans,s,-1):
        print(ans)
        return
    ans = make("WW",n,s)
    if check(ans,s,0) and check(ans,s,-1):
        print(ans)
        return
    print(-1)
    return

if __name__ == "__main__":
    solve()
