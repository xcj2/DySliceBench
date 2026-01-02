def A():
    temp = input().split()
    S = temp[0]
    T = temp[1]
    temp = [int(i) for i in input().split()]
    A = temp[0]
    B = temp[1]
    U = input()
    if U == S:
        print(A-1, B)
    else:
        print(A, B-1)

def B():
    print('x'*len(input()))

def C():
    N = int(input())
    A = [int(i) for i in input().split()]
    if N > len(set(A)):
        print('NO')
    else:
        print('YES')

def D():
    temp = [int(i) for i in input().split()]
    N = temp[0]
    K = temp[1]
    p = [int(i) for i in input().split()]
    expected_val = [(i+1)/2.0 for i in p]
    cur = sum(expected_val[:K])
    ans = cur
    for i in range(N-K):
        cur -= expected_val[i]
        cur += expected_val[i+K]
        ans = max(ans, cur)
    print(ans)

def E():
    #https://www.geeksforgeeks.org/count-of-numbers-in-range-where-the-number-does-not-contain-more-than-k-non-zero-digits/
    def countInRangeUtil(pos, cnt, tight, num): 
        if pos == len(num): 
            if cnt == K: 
                return 1
            return 0
    
        if dp[pos][cnt][tight] != -1: 
            return dp[pos][cnt][tight] 
    
        ans = 0
    
        limit = 9 if tight else num[pos] 
    
        for dig in range(limit + 1): 
            currCnt = cnt 
    
            if dig != 0: 
                currCnt += 1
    
            currTight = tight 
    
            if dig < num[pos]: 
                currTight = 1
    
            ans += countInRangeUtil(pos + 1, currCnt, currTight, num) 
    
        dp[pos][cnt][tight] = ans 
        return dp[pos][cnt][tight] 

    global dp, K, M 
    N = int(input())
    K = int(input())
    M = 100
  
    num = [] 
    while N: 
        num.append(N % 10) 
        N //= 10
  
    num.reverse() 
  
    # Initialize dp 
    dp = [[[-1, -1] for i in range(M)] for j in range(M)] 
    print(countInRangeUtil(0, 0, 0, num)) 
  

E()