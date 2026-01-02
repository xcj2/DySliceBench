n = input()
k = int(input())

l = len(n)
n = int(n)

ans=0

def one(n):
    l = len(str(n))
    ans = 9 * (l-1)
    ans += n//(10**(l-1))
    return ans

def two(n):
    l = len(str(n))
    ans = 0
    if l == 1:
        return 0
    elif l == 2:
        ans = (n//10-1) *9 + n%10
        return ans
    else:
        ans +=   81 * (l-1) * (l-2) // 2
        # print(81*5*4/2)
        # print(ans)
        t = n % (10**(l-1))
        ans += one(t) + one(10**(l-1)-1)* (n// (10**(l-1))-1)
        return ans

def three(n):
    l = len(str(n))
    ans = 0
    if l <= 2:
        # print(n)
        return ans
    elif l == 3:
        ans = (n//100-1) * two(99) + two( n % 100 )
        return  ans
    else:
        ans = 729 * (l-1) * (l-2) * (l-3) // 6
        t = n % (10**(l-1))
        ans += two(t) + two(10**(l-1)-1)* (n// (10**(l-1))-1)
        return ans
    return ans

if k == 1:
    ans = one(n)
if k == 2:
    ans = two(n)
if k == 3:
    ans = three(n)

if l <= 3 and n != one(n) + two(n) + three(n):
    print(one(n),two(n),three(n))
    print("Error!")

print(ans)

# 100000 ~ 314159 

# print()

# n=9 k=1:9
# n=99 k=1:18 k=2:81=81*2C2
# n=999 k=1:27 k=2:81*3=243,81*(3C2) k=3:9^3=729 = 729*3C3
# n=9999 k=1:9*4, k=2:81*4C2, K=3:729*4C3=

# k=2, 1,2,6,10,15,

# n=515 nの桁数:d=3 10^(d-1)=100 515/100=5 100,200,300,400,500 18+5=23
# n=515, k=2:101~109,110,120,130~190,201~209
# n=250,18,
# k=2,1001-1009,1010,1020...1090,1100,1200..1900 27*9=243
# k=2を求めるよりも、k<=2を求めてからk=1を求める方が簡単か? そんなこともないか