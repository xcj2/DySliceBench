def check(mid,n):
    total = 26*(pow(26,mid)-1)//25
    if total <= n:
        return True

    return False

def find(n):
    low = 1
    high = 10
    x = 0
    while low <= high:
        mid = (low+high)//2
        if check(mid,n):
            x = mid
            low = mid+1
        else:
            high = mid-1

    return x

def find2(n,x,curr_len):
    low = 0
    high = 26
    while low <= high:
        mid = (low+high)//2
        if mid*pow(26,x-curr_len-1) < n:
            low = mid+1
            k = mid
        else:
            high = mid-1

    return k

def main():
    n = int(input())
    if n <= 26:
        print(chr(ord('a')+n-1))
        return
    
    ans = ''
    x = find(n)
    n -= 26*(pow(26,x)-1)//25
    if n == 0:
        for i in range(x):
            ans += 'z'
    else:
        x += 1
        #print(n)
        while len(ans) != x:
            k = find2(n,x,len(ans))
            if k == 0:
                ans += chr(ord('a')+k)
            else:
                ans += chr(ord('a')+k)
                n -= k*pow(26,x-len(ans))

            #print(ans,n,k)

    print(ans)
            
    
main()
