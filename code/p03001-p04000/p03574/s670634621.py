h,w=[int(i) for i in input().split()]

masu=[]
for i in range(h):
    masu.append(list(input()))

def top(i,j):
    ans=0
    if i==0:
        pass
    else:
        check=masu[i-1][max(0,j-1):min(w,j+2)]
        ans+=check.count("#")
    return ans

def bottom(i,j):
    ans=0
    if i==h-1:
        pass
    else:
        check=masu[i+1][max(0,j-1):min(w,j+2)]
        ans+=check.count("#")
    return ans

def side(i,j):
    ans=0
    check=masu[i][max(0,j-1):min(w,j+2)]
    ans+=check.count("#")
    return ans
    
def mawari(i,j):
    taishou=masu[i][j]
    if taishou==".":
        return str(top(i,j)+bottom(i,j)+side(i,j))
    else:
        return "#"

answer=[]
for i in range(h):
    gyou=[]
    for j in range(w):
        gyou.append(mawari(i,j))
    answer.append("".join(gyou))
    
for i in answer:
    print(i)