from collections import defaultdict

def lcm_dict(A):
    pf_d=defaultdict(int)
    for num in A:
        for k in range(2,int(num**0.5)+1):
            cnt=0
            while num%k==0:
                cnt+=1
                num//=k
            if cnt:
                pf_d[k]=max(pf_d[k],cnt)
        if num!=1:
            pf_d[num]=max(pf_d[num],1)
    return pf_d

def modinv(k,mod):
    return pow(k,mod-2,mod)

def main():
    mod=1000000007
    n=int(input())
    A=tuple(map(int,input().split()))
    lcm_d=lcm_dict(A)
    l=1
    for num in lcm_d:
        cnt=lcm_d[num]
        l*=pow(num,cnt,mod)
        l%=mod
    ans=0
    for a in A:
        ans+=l*modinv(a,mod)
        ans%=mod
    print(ans)

if __name__=='__main__':
    main()