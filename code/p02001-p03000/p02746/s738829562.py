#解説を写経することは最高に悪魔的な行為だ…
def between(x,y1,y2):
    if y1>y2:y1,y2=y2,y1
    y1+=1;y2-=1
    if not(y1<=y2):
        return False
    while(x>0):
        if x%3==1:
            if y2-y1>3:
                return True
            for y in range(y1,y2+1):
                if y%3==1:
                    return True
        x//=3
        y1//=3
        y2//=3
    return False
def get_extra(x1,y1,x2,y2):
    ans=0
    three=1
    for i in range(35):
        if(x1//three==x2//three and between(x1//three,y1//three,y2//three)):
            tmp=min(min(x1%three,x2%three)+1,three-max(x1%three,x2%three))
            ans=max(ans,tmp)
        three*=3
    return ans
def get_dist(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)+2*max(get_extra(x1,y1,x2,y2),get_extra(y1,x1,y2,x2))
Q=int(input())
for i in range(Q):
    a,b,c,d=map(int,input().split())
    print(get_dist(a-1,b-1,c-1,d-1))