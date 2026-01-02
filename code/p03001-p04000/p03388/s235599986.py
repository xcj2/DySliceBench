import math

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

def max_multi(a,b,d,c):
        length = b-a
        n = math.ceil((d-a)/2)
        if n < 0:
            n = 0
        elif n > length:
            n = length
        x = (a+n)*(d-n)
        n = math.floor((d-a)/2)
        if n < 0:
            n = 0
        elif n > length:
            n = length
        y = (a+n)*(d-n)
        return max(x,y)

def check(a, b, n):
    multi = a*b
    if n<a:
        return True
    else:
        if a<= n < b:
            #second_1 = [i for i in range(1, n+1)][::-1]
            second_1 = (n,1)
            second_2 = (0,0)
        else:
            #second_1 = [i for i in range(1, b)][::-1]
            second_1 = (b-1,1)
            #second_2 = [i for i in range(b+1, n+2)][::-1]  
            second_2 = (n+1, b+1)
        m = (second_2[0] - second_2[1])+1
        #print('m :', m)
        if second_2 == (0,0):
            a1,b1,c1,d1 = 1, a-1, second_1[0], second_1[0]-(a-2)
            a2,b2,c2,d2 = a+1, n+1, second_1[0]-(a-1), second_1[1]
            #print(a1,b1,c1,d1)
            #print(a2,b2,c2,d2)
            s = max(max_multi(a1,b1,c1,d1), max_multi(a2,b2,c2,d2))
        elif m == a-1:
            a1,b1,c1,d1 = 1, a-1, second_2[0], second_2[1]
            a2,b2,c2,d2 = a+1, n+1, second_1[0], second_1[1]
            #print(a1,b1,c1,d1)
            #print(a2,b2,c2,d2)
            #print(max_multi(a1,b1,c1,d1), max_multi(a2,b2,c2,d2))
            s = max(max_multi(a1,b1,c1,d1), max_multi(a2,b2,c2,d2))
        elif m > a-1:
            a1,b1,c1,d1 = 1, a-1, second_2[0], second_2[0]-(a-2)
            a2,b2,c2,d2 = a+1, m+1, second_2[0]-(a-1), second_2[1]
            a3,b3,c3,d3 = m+2, n+1, second_1[0], second_1[1]
            #print(a1,b1,c1,d1)
            #print(a2,b2,c2,d2)
            #print(a3,b3,c3,d3)
            s = max(max_multi(a1,b1,c1,d1), max_multi(a2,b2,c2,d2), max_multi(a3,b3,c3,d3))
        else:
            a1,b1,c1,d1 = 1,m,second_2[0], second_2[1]
            a2,b2,c2,d2 = m+1, a-1, second_1[0], second_1[0]-(a-m-2)
            a3,b3,c3,d3 = a+1, n+1, second_1[0]-(a-m-1), second_1[1]
            #print(a1,b1,c1,d1)
            #print(a2,b2,c2,d2)
            #print(a3,b3,c3,d3)
            s = max(max_multi(a1,b1,c1,d1), max_multi(a2,b2,c2,d2), max_multi(a3,b3,c3,d3))
        return True if s < multi else False

def search(a,b):
    a,b = min(a,b), max(a,b)
    low = 0
    high = 10**30
    while high - low > 1:
        if check(a,b,(low+high)//2):
            low = (low+high)//2
            #print('low :', low)
        else:
            high = (low+high)//2
            #print('high :', high)
    return high if check(a,b,high) else low

for i in lst:
    print(search(i[0], i[1]))