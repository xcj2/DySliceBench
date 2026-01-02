import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    dic = collections.defaultdict(int)

    while n != 1:
        prime = 0
        limit = int(n**(1/2))
        for i in range(2,limit+1):
            if n%i == 0:
                prime = i
                break
        else:
            prime = n

        while n%prime == 0:
            n //= prime
            dic[prime] += 1

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
