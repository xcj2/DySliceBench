def factorize(n):
    i=2
    result={}
    while True:
        if i**2>n:
            break
        count=0
        while n%i==0:
            n//=i
            count+= 1
        if count!=0:
            result[i]=count
        i+=1
    if n>1:
        result[n]=1
    return result

def count(v):
    cnt=0
    num=1
    while cnt<=v:
        cnt+=num
        num+=1
        #print(cnt,num)
    return num-2

def main():
    n=int(input())
    F=factorize(n)
    #print(F)
    ans=0
    for val in F.values():
        #print(val,count(val))
        ans+=count(val)
    print(ans)
    
if __name__=='__main__':
    main()