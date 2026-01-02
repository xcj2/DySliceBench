def readinput():
    n=int(input())
    x=input()
    return n,x

poptbl=[0]*(2*10**5+1)
def popcount(x):
    global poptbl
    if poptbl[x]!=0:
        return poptbl[x]
    
    poptbl[x]=bin(x).count('1')
    return poptbl[x]

ftbl=[0]*(2*10**5+1)
def f(x):
    global ftbl

    if ftbl[x]!=0:
        return ftbl[x]
    
    #print('f(x), x: {}'.format(x))
    if x==0:
        return 0
    else:
        ans=f(x%popcount(x))+1
        #print(ans)
        ftbl[x]=ans
        return ans    

def main():
    n=int(input())
    x=input()
    m=x.count('1')
    #print('m: {}'.format(m))
    xint=int(x,2)
    #print('xint: {}'.format(xint))
    if m!=1:
        xmodm1=xint%(m-1)
    else:
        xmodm1=1
    xmodp1=xint%(m+1)
    pow2mod1=[0]*n
    pow2mod2=[0]*n
    pow2mod1[0]=1
    pow2mod2[0]=1
    for i in range(1,n):
        if m!=1:
            pow2mod1[i]=pow2mod1[i-1]*2 % (m-1)
        pow2mod2[i]=pow2mod2[i-1]*2 % (m+1)

    ans=[]
    #b=2**(n-1)
    for i in range(n):
        if x[i]=='1':
            if m==1:
                a=0
                ans.append(a)
            else:
                xx=( xmodm1 + (m-1) -pow2mod1[n-i-1] )%(m-1)
                #ans.append(f(xx)+1)
                a=f(xx)+1
                ans.append(a)
        else:
            xx=( xmodp1 + pow2mod2[n-i-1] )%(m+1)
            #ans.append(f(xx)+1)
            a=f(xx)+1
            ans.append(a)
        #b=b//2
        print(a)
    return ans

if __name__=='__main__':
    #n,x=readinput()
    ans=main()
    #for a in ans:
    #    print(a)

