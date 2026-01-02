import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    def prime_factor(n):
        lst = []
        while n%2 == 0:
            n //= 2
            lst.append(2)
        f = 3
        while f**2 <= n:
            if n%f == 0:
                n //= f
                lst.append(f)
            else:
                f += 2
        if n != 1:
            lst.append(n)
        return lst
    dic = collections.Counter(prime_factor(n))
    ans = 0

    for key,value in dic.items():
        cnt = 0
        while value>=cnt+1:
            cnt += 1
            value -= cnt

        ans += cnt
    # print(dic)
    print(ans)
        
main()            
