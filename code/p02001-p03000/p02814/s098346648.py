#python3

def gcd(x, y):
    if x % y == 0:
        return y
    return gcd(y, x%y)

def lcm(x, y):
    return (x * y) //gcd(x, y) 

def f(x):
    res = 0
    while x % 2 == 0:
        x //= 2
        res += 1
    return res 

def main():
    n, m = map(int, input().split())
    a = [int(i)//2 for i in input().split()]

    t = f(a[0])
    for i in range(n):
        if f(a[i]) != t:
            print(0)
            return
        a[i] //= 2**t; 

    m //= 2**t
    l = 1
    for i in range(n):
        l = lcm(l, a[i])
        if l > m:
            print(0)
            return

    m //= l
    ans = (m+1)//2
    print(ans)
main()

