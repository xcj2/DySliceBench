N = int(input())
#num = [1]
#print("a")
"""
#memo = [[ -1 for i in range(12)]for j in range(100000)]
n = 6
while True:
    num.append(n)
    n *= 6
    if n > 100000:
        break
n = 9
while True:
    num.append(n)
    n *= 9
    if n > 100000:
        break
num.sort()

ans = 0
print(num)
#while N > 6:

def DP(n , index):
    if index == 0:
        return  n
    elif n == 0:
        return 0
    min_ = 10000000
    if n < num[index]:
        #print(n,num[index])
        return DP(n,index - 1)
    can = num[index]
    #print(index)
#    print(n//can)
    for i in range(n // can+1):
        min_ = min(min_ , DP(n - i * can,index - 1) + i)
 #       print(i,n,index,DP(n - i*can,index-1))
    
     #   print(min_)
    #print(min_)
    memo[n][index] = min_
    return min_
    
print(DP(N,11))
"""

def ninep(N):
    if N <9:
        return N
    ans = 0
    while N > 0:
        ans += N % 9
        N =N // 9
    return ans


def sixp(N):
    if N <6:
        return N
    ans = 0
    while N > 0:
        ans += N % 6
        N = N // 6
    return ans


ans = 1000000
for i in range(N+1):
    ans = min(ans,ninep(i) + sixp(N - i))
#    print(ninep(i), sixp(N - i),i)

print(ans)
