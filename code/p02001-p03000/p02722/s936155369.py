def factorize_dict(n):
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

def make_divisors(n):
    divisors=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            divisors.append(i)
            if i!=n//i:
                divisors.append(n//i)
    return divisors

def judge(n,k):
    while n%k==0:
        n//=k
    return n%k

def main():
    n=int(input())
    ans=0
    f_d=factorize_dict(n-1)
    tmp=1
    for v in f_d.values():
        tmp*=(v+1)
    tmp-=1
    ans+=tmp
    D=make_divisors(n)
    for d in D:
        if d==1:
            continue
        if judge(n,d)==1:
            ans+=1
    print(ans)
    
if __name__=='__main__':
    main()