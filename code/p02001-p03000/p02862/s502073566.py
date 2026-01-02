import math
mod = (10**9) + 7

def kaijo(n):
    result = 1
    for i in reversed(range(1,n+1)):
        result = (result * i) % mod
    return result
def combinations_count(n, r):
    return (kaijo(n)) //(kaijo(n - r) * kaijo(r))

def nCk(n, k):
    ret = 1
    mo = 10**9 + 7
    for i in range(k):
        ret = ret * (n - i) * pow(i + 1, mo - 2, mo) % mo
    return ret


X,Y = map(int,input().split(' '))

if (X+Y)%3 == 0:
    flag = False
    if X > Y:
        diff = X - Y
        all_num = (X+Y)//3
        count_2 = Y - all_num
        if X > Y*2:
            flag = True
    elif Y > X:
        diff = Y - X
        all_num = (X+Y)//3
        count_2 = X - all_num
        if Y > X*2:
            flag = True
    else:
        all_num = (X+Y)//3
        count_2 = all_num//2
    if flag:
        print(0)
    else:
        print(nCk(all_num,count_2))
else:
    print(0)