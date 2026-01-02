N,X = map(int,input().split())

"""
　　レベルnの層数：a_0 = 1 , a_n = 2*a_(n-1)+3
レベルnのパティ数：b_0 = 1 , b_n = 2*b_(n-1)+1
"""

def thickness(n):
    if n == 0:
        return 1
    else:
        return 2 * thickness(n-1) + 3

def patty(n):
    if n == 0:
        return 1
    else:
        return 2 * patty(n-1) + 1

def ans(n,x):
    if n == 0:
        return 1
    else:
        if x == 1:
            return 0
        if 1 < x <= thickness(n-1)+1:
            return ans(n-1,x-1)
        if x == thickness(n-1) + 2:
            return patty(n-1) + 1
        if thickness(n-1) + 2 < x <= 2 * thickness(n-1) + 2:
            return patty(n-1) + 1 + ans(n-1,x-2-thickness(n-1))
        if x == 2 * thickness(n-1) + 3:
            return 2 * patty(n-1) + 1

print(ans(N,X))
