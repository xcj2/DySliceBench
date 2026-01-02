def get_switch(n):
    allswitch = []
    for i in range(0,2**n):
        bin_str = format(i,'0'+str(n)+'b')
        swt = list(map(int,list(bin_str)))
        allswitch.append(swt)
    return allswitch

def test(patarn,a,x,y,n):
    ans_sub=sum(patarn)
    for i in range(n):
        if patarn[i]==1:
            for j in range(a[i]):
                if y[i][j]==1:
                    if patarn[x[i][j]]==0:
                        return 0
                else:
                    if patarn[x[i][j]]==1:
                        return 0
        #else:
            #f.append(i)
            #if i in t:
                #return 0
    #print(patarn)
    return ans_sub
    
def main():
    n=int(input())
    a=[]
    x=[]
    y=[]
    for i in range(n):
        a_sub=int(input())
        a.append(a_sub)
        x_sub=[]
        y_sub=[]
        for j in range(a_sub):
            tmp=list(map(int,input().split()))
            x_sub.append(tmp[0]-1)
            y_sub.append(tmp[1])
        x.append(x_sub)
        y.append(y_sub)
    #print(x)
    #print(y)
    ans=0
    for patarn in get_switch(n):
        ans=max(ans,test(patarn,a,x,y,n))
    print(ans)

if __name__=='__main__':
    main()