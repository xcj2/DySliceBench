def readinput():
    n=int(input())
    return n

def main(n):
    fk=[1]*(n+1)
    for i in range(2,n+1):
        j=i
        while(j<=n):
            fk[j]+=1
            j+=i
    sum=0
    for i in range(1,n+1):
        sum+=i*fk[i]
    return sum

def main2(n):
    fk=[]
    for i in range(n+1):
        fk.append(i)
    for i in range(2,n+1):
        j=i
        while(j<=n):
            fk[j]+=j
            j+=i
    sum=0
    for i in range(1,n+1):
        sum+=fk[i]
    return sum

if __name__=='__main__':
    n=readinput()
    ans=main2(n)
    print(ans)
