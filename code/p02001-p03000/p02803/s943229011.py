import copy

def judge1(masu,h,w):
    if (masu[0]>=0)&(masu[0]<h)&(masu[1]>=0)&(masu[1]<w):
        return True
    else:
        return False
    
def judge2(masu,s):
    if s[masu[0]][masu[1]] == '.':
        return True
    else:
        return False
    
def tsugi(i,j,h,w,s2):
    ans=[]
    for masu in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
        if judge1(masu,h,w):
            if judge2(masu,s2):
                ans.append(masu)
    return ans
    


def solve(i,j,s,h,w):
    ma = 0
    s2 = copy.deepcopy(s)
    if s2[i][j]=='.':
        s2[i][j]='#'
        nex = tsugi(i,j,h,w,s2)
        while len(nex)!=0 :
            ma+=1
            nex2=[]
            for n in nex:
                nex2[len(nex2):] = tsugi(n[0],n[1],h,w,s2)
                s2[n[0]][n[1]]='#'
            nex = set(nex2)
    return ma


h,w=map(int,input().split())
s = []
ma = 0
for i in range(h):
    s.append(list(input()))
for i in range(h):
    for j in range(w):
        ans = solve(i,j,s,h,w)
        ma = max(ma,ans)
print(ma)

