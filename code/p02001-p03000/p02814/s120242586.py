import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def gcd(x, y):
    if x%y == 0:
        return y
    return gcd(y, x%y)

def lcm(x, y):
    return x*y//gcd(x, y)

def f(x):
    res = 0
    while x%2 == 0:
        x//=2
        res += 1
    return res

def main():
    N, M = map(int, readline().split())
    A = [int(i)//2 for i in readline().split()]

    t = f(A[0]) 
    for i in A:
        if f(i) != t:
            print(0)
            return

    A = [i//(2**t) for i in A] 
    M //= 2**t    

    l = 1
    for i in A:
        l = lcm(l, i)
        if l > M:
            print(0)
            return
    M //= l
    ans = (M+1)//2
    print(ans)
if __name__ == '__main__':
    main()