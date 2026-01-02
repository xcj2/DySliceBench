# -*- coding: utf-8 -*-

EDPC = "https://atcoder.jp/contests/dp/"
TDPC = "https://atcoder.jp/contests/tdpc/tasks"


################ DANGER ################
test = ""

########################################
test = list(reversed(test.strip().splitlines()))
if test:
    def input2():
        return test.pop()
else:
    def input2():
        return input()
########################################  


def maximized(a):
    """
    1 -2 3 -4 5
    全探索より速い 
    """
    dp = [0] * (len(a) + 1)
    for i in range(len(a)):
        dp[i+1] = max(dp[i], dp[i] + a[i])
    return dp[-1]


def A_Frog1(a):
    """
    '''
    4
    10 30 40 20
    ans 30
    '''
    '''
    2
    10 10
    ans 0
    '''
    '''
    6
    30 10 60 10 60 50
    ans 40
    '''
    """
    n, h = len(a), a
    dp = [0] * n
    dp[0] = 0
    dp[1] = abs(h[1] - h[0])
    for i in range(1, n - 1):
        dp[i+1] = min(
                dp[i-1] + abs(h[i+1] - h[i-1]), 
                dp[i] + abs(h[i+1] - h[i]))
    return dp[-1]
    
    

if __name__ == "__main__":
    ################## IO ##################
    input2()
    a = list(map(int, input2().split()))
    print(A_Frog1(a))
    
    
    
    