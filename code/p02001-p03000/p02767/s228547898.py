def readinput():
    n=int(input())
    x=list(map(int,input().split()))
    return n,x

def mean(x):
    sum=0
    for _ in x:
        sum+=_
    return sum/len(x)

def rss(x,xbar):
    sum=0
    for _ in x:
        sum+=(_-xbar)**2
    return sum

def main(n,x):
    ans=0
    xbar=mean(x)
    xbar_int=xbar//1
    if(xbar-xbar_int >0.5):
        xbar_int+=1
    ans=rss(x,xbar_int)
    return int(ans)

def main2(n,x):
    xmin=min(x)
    xmax=max(x)
    minsum=1000000

    for p in range(xmin,xmax+1):
        sum=0
        for xx in x:
            sum+=(xx-p)**2
        if(sum<minsum):
            minsum=sum

    return minsum

if __name__=='__main__':
    n,x=readinput()
    ans=main(n,x)
    print(ans)
