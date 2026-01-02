from collections import Counter
def min_fac_array(n):
    nums = [i for i in range(n+1)]
    for i in range(2,n+1):
        if nums[i] == i:
            for j in range(2*i,n+1,i):
                if nums[j] == j:
                    nums[j] = i
    return nums

def fac_fast(mfa,a):
    n = a
    fac = []
    while n != 1:
        fac.append(mfa[n])
        n //=mfa[n]
    return fac

def main(): 
    n = int(input())
    mfa = min_fac_array(n)
    ans = 1
    for i in range(2,n):
        fac = fac_fast(mfa,i)
        dic = Counter(fac)
        temp = 1
        for p in dic.values():
            temp*=p+1
        ans+=temp
    
    print(ans)
main()