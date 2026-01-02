def m(n): # n次元バーガーの層数
    if n == 0:
        return 1
    else:
        a = 1
        for i in range(n):
            a = a * 2 + 3
        return a

def paty(n): # n次元バーガーのパティの数
    a = 1
    if n >= 1:
        for i in range(n):
            a = a * 2 + 1
    return a

def a(n, x): #これが答えを返す
    x = x - 1
    if x == 0 and n == 0:
        return 1
    elif x == 0:
        return 0
    elif x == m(n-1) + 1:
        return paty(n-1) + 1
    elif x == m(n):
        return paty(n)
    elif x > m(n-1):
        return paty(n-1) + 1 + a(n - 1, x - m(n-1) - 1)
    else:
        n = n - 1
        return a(n, x)

n, x= map(int, input().split())
print(a(n, x))