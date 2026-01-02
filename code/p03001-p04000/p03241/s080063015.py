# import string
import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():

    n,m=map(int,input().split())
    def make_divisors(n):
        divisors = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i: # 平方数の場合n**0.5を1つだけにしてる
                    divisors.append(n//i)

        divisors.sort(reverse=True) # ソートしたけりゃして
        return divisors
    l=make_divisors(m)
    for i in l:
        if n*i<=m:
            print(i)
            break



resolve()